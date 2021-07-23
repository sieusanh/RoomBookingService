from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import RoomBooking
from .serializers import RoomBookingSerializer
from datetime import datetime, timedelta
from Apps.Room.models import RoomType, RoomStatus


# Create your views here.
class RoomBookingView(APIView):

    def get(self, request):
        return Response(data="Room Booking Site", status=status.HTTP_200_OK)

    def put(self, request):
    
        # Update data on other models

        # RoomBooking
        mydata = RoomBookingSerializer(data=request.data)

        RoomType_Code = request.session.get('RoomCode')
        Customer_Code = request.session.get('CustomerCode')
        Start_Date = mydata.data['StartDate']
        End_Date = mydata.data['EndDate']
        Booking_Date = datetime.today().strftime('%Y-%m-%d')
        Unit_Price = request.session.get('UnitPrice')
        Description = mydata.data['Description']
        Status = mydata.data['Status']

        RoomBooking.objects.create(
        RoomTypeCode=RoomType_Code, 
        CustomerCode=Customer_Code, 
        StartDate=Start_Date, 
        EndDate=End_Date, 
        BookingDate=Booking_Date, 
        UnitPrice=Unit_Price, 
        Description=Description, 
        Status=Status)

        # Apps.Room.models.RoomStatus
        Room_Code = request.session.get('RoomCode')
        RoomStatusList = RoomStatus.objects.filter(RoomCode=Room_Code)
        RoomStatusList.delete()
        i = Start_Date
        delta = timedelta(days=1)
        while i <= End_Date:
            RoomStatus().objects.create(RoomCode=Room_Code, Date=i, Status=(1, 'đang sử dụng'))
            i += delta

        # Apps.Room.models.RoomType
        try:
            Room_Type = RoomType.objects.get(RoomTypeCode=RoomType_Code)
        except ObjectDoesNotExist:
            return Response('Mã loại phòng không tồn tại', status=status.HTTP_404_NOT_FOUND)
        Room_Type.VacancyAmount -= 1
        Room_Type.save()

        return Response('Đặt phòng thành công', status=status.HTTP_200_OK)