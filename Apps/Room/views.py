from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import RoomType, Room, RoomStatus
from Apps.Hotel.views import HotelModel
from Apps.Hotel.serializers import HotelSearchSerializer, HotelChooseSerializer
from .serializers import RoomTypeChooseSerializer, RoomChooseSerializer, DateSerializer, RoomStatusUpdateSerializer
from django.db.models import Q


# Create your views here.
# Booking Room Business Process
# Step 1: User choose Hotel and Room
    # a) Search Hotel and choose
    # b) Search Room Type and choose 
    # c) Search Room and choose

# Step 2: System check if the booking process is valid

# Step 3: If the booking infomation is valid, the system will save the booking information in database.
#         If not, the system will notice occupied rooms and require user to choose again.

# Muốn thức hiện thức năng này phải thực hiện chức năng đăng nhập trước
# Hotel Search and Choose View 
class HotelSearchView(APIView):

    def get(self, request):
        if not request.user.is_authenticated:
            return Response('Vui lòng đăng nhập để thực hiện chức năng này', status=status.HTTP_200_OK)
        return Response('Hotel Search View get method', status=status.HTTP_200_OK)
        '''
        mydata = HotelSearchSerializer(data=request.data)
        if not mydata.is_valid():
            return Response('Nhập thông tin tìm kiếm Khách sạn không hợp lệ', status=status.HTTP_400_BAD_REQUEST)
        
        HotelList = HotelModel.objects.filter( 
        (Q(City=mydata.data['City']) & Q(AveragePrice=mydata.data['AveragePrice'])) 
        | (Q(City=mydata.data['City']) & Q(StarType=mydata.data['StarType']))
        )
        
        if not HotelList.exists():
            HotelList = HotelModel.objects.filter(City=mydata.data['City'])
        return Response(data=HotelList.values(), status=status.HTTP_200_OK)
        '''
    
    def post(self, request):
        return Response("Post method Room_HotelSearch")
        '''
        mydata = HotelChooseSerializer(data=request.data)
        if not mydata.is_valid():
            return Response('Nhập thông tin chọn Khách sạn không hợp lệ', status=status.HTTP_400_BAD_REQUEST)
        
        # pass data between views in django using Django session variables
        request.session['HotelCode'] = mydata.data

        return redirect('RoomType')
        '''

# Room Type Search and Choose View 
class RoomTypeSearchView(APIView):

    def get(self, request):

        Hotel_Code = request.session.get('HotelCode')

        RoomTypeList = RoomType.objects.filter(HotelCode=Hotel_Code)
        if not RoomTypeList.exists():
            return Response(data="Không tồn tại Bất kỳ loại Phòng nào cho Khách sạn vừa được chọn", 
            status=status.HTTP_404_NOT_FOUND)
        
        return Response(data=RoomTypeList, status=status.HTTP_200_OK)
    
    def post(self, request):
        
        mydata = RoomTypeChooseSerializer(data=request.data)
        if not mydata.is_valid():
            return Response('Nhập thông tin chọn Loại phòng không hợp lệ', status=status.HTTP_400_BAD_REQUEST)
        
        try:
            room_type = RoomType.objects.get(RoomTypeCode=mydata.data)
        except ObjectDoesNotExist:
            return Response(data="Mã loại phòng không tồn tại", status=status.HTTP_404_NOT_FOUND)
        if room_type.VacancyAmount == 0:
            return Response(data="Hiện tại không còn phòng trống cho loại phòng này", status=status.HTTP_404_NOT_FOUND)

        request.session['RoomTypeCode'] = mydata.data
        p = RoomType.objects.get(RoomTypeCode=mydata.data)
        request.session['UnitPrice'] = p.UnitPrice
        
        return redirect('Room')

# Room Search and Choose View
class RoomSearchView(APIView):
    def get(self, request):

        RoomType_Code = request.session.get('RoomTypeCode')

        RoomList = Room.objects.filter(RoomType=RoomType_Code)
        if not RoomList.exists():
            return Response(data="Không tồn tại Bất kỳ Phòng nào cho Mã loại phòng vừa được chọn", 
            status=status.HTTP_404_NOT_FOUND)

        return Response(data=RoomList, status=status.HTTP_200_OK)

    def post(self, request):

        mydata = RoomChooseSerializer(data=request.data)
        if not mydata.is_valid():
            return Response('Nhập thông tin chọn Phòng không hợp lệ', status=status.HTTP_400_BAD_REQUEST)

        request.session['RoomCode'] = mydata.data

        return redirect('RoomStatusSearch')

class RoomStatusSearchView(APIView):

    def get(self, request):

        Room_Code = request.session.get('RoomCode')
        Date = DateSerializer(data=request.data)

        try:
            Room_Status = RoomStatus.objects.get(RoomCode=Room_Code, Date=Date)
        except ObjectDoesNotExist:
            return Response(data='Mã phòng không tồn tại hoặc Trạng thái phòng không xác định', status=status.HTTP_404_NOT_FOUND)
        if Room_Status.Status == 0:
            return Response(data='Phòng còn trống', status=status.HTTP_200_OK)
        elif Room_Status.Status == 1:
            return Response(data='Phòng đang được sử dụng', status=status.HTTP_200_OK)
        else:
            return Response(data='Phòng đang bảo trì', status=status.HTTP_200_OK)
    
    def post(self, request):
        
        return redirect('Apps.Booking.views.RoomBooking')

class RoomStatusUpdateView(APIView):

    def get(self, request):
        return Response("Room Status Update View", status=status.HTTP_200_OK)

    def put(self, request):
        mydata = RoomStatusUpdateSerializer(data=request.data)

        try:
            Room_Status = RoomStatus.objects.get(RoomCode=mydata['RoomCode'], Date=mydata['Date'])
        except ObjectDoesNotExist:
            return Response(data='Mã phòng không tồn tại hoặc Trạng thái phòng không xác định', status=status.HTTP_404_NOT_FOUND)

        if mydata['Status'] == 0:
            Room_Status.Status = (0, 'còn trống')
        elif mydata['Status'] == 1:
            Room_Status.Status = (1, 'đang sử dụng')
        else:
            Room_Status.Status = (2, 'đang bảo trì')
        Room_Status.save()

        return Response(data='Cập nhật Trạng thái phòng thành công', status=status.HTTP_200_OK)