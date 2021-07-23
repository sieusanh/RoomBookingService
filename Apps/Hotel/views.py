from django.shortcuts import render
from django.core import serializers
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import HotelSearchSerializer, AddNewHotelSerializer
from .models import HotelModel


# Create your views here.

# Add new hotel to database
class AddNewHotelView(APIView):

    def get(self, request):
        return Response('Add New Hotel View', status=status.HTTP_200_OK)

    def post(self, request):
        mydata = AddNewHotelSerializer(data=request.data)

        if not mydata.is_valid():
            return Response('Nhập thông tin khách sạn không hợp lệ', status=status.HTTP_400_BAD_REQUEST)
        new_hotel = HotelModel.objects.create(HotelName=mydata.data['HotelName'], StarType=mydata.data['StarType'], 
        HouseNumber=mydata.data['HouseNumber'], Street=mydata.data['Street'], 
        District=mydata.data['District'], City=mydata.data['City'], 
        AveragePrice=mydata.data['AveragePrice'], Description=mydata['Description'])
        return Response('Thêm khách sạn thành công', status=status.HTTP_200_OK)

# Hotel Search View
class HotelSearchView(APIView):

    def get(self, request):

        mydata = HotelSearchSerializer(data=request.data)

        if not mydata.is_valid():
            return Response('Nhập thông tin tìm kiếm không hợp lệ', status=status.HTTP_400_BAD_REQUEST)
        #HotelList = list()
        '''
        if mydata.data['StarType'] is not None or mydata.data['StarType'] != 0:
            HotelList = HotelModel.objects.filter(StarType=mydata.data['StarType'], City=mydata.data['City'])
            return Response(data=HotelList.values(), status=status.HTTP_200_OK)

        if mydata.data['AveragePrice'] is not None or mydata.data['AveragePrice'] != 0:
            HotelList = HotelModel.objects.filter(AveragePrice=mydata.data['AveragePrice'], City=mydata.data['City'])
            return Response(data=HotelList.values(), status=status.HTTP_200_OK)
        '''    
    
        HotelList = HotelModel.objects.filter( 
        (Q(City=mydata.data['City']) & Q(AveragePrice=mydata.data['AveragePrice'])) 
        | (Q(City=mydata.data['City']) & Q(StarType=mydata.data['StarType']))
        )
        if not HotelList.exists():
            HotelList = HotelModel().objects.filter(City=mydata.data['City'])
            #serialized_queryset = serializers.serialize('json', HotelList)
        return Response(data=HotelList.values(), status=status.HTTP_200_OK)
        
    def post(self, request):
        pass
