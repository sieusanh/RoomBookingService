from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .factories import (
    CustomerUserFactory,
    StaffUserFactory,
    HotelModelFactory,
    RoomTypeFactory,
    RoomFactory,
    RoomStatusFactory,
    RoomBookingFactory,
    BillingFactory
)

from Apps.User.models import CustomerUser, StaffUser
from Apps.Hotel.models import HotelModel
from Apps.Room.models import RoomType, Room, RoomStatus
from Apps.Booking.models import RoomBooking
from Apps.Checkout.models import Billing

#import random
from django.db import transaction
import time

CUSTOMER_USER_NUMBER = 10000
STAFF_USER_NUMBER = 500
HOTEL_NUMBER = 500
ROOM_TYPE_NUMBER = 700
ROOM_NUMBER = 5000
ROOM_STATUS_NUMBER = 12000
ROOM_BOOKING_NUMBER = 8000
BILLING_NUMBER = 8000

def convert_time(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds)

# Create your views here.
class DataGeneratorView(APIView):
    
    def get(self, request):
        s = "Welcome to Data Generator View\n"
        s += "The system has generated: \n"
        
        s += str(CustomerUser.objects.filter().count()) + " CustomerUser rows\\n"
        s += str(StaffUser.objects.filter().count()) + " StaffUser rows\\n"
        s += str(HotelModel.objects.filter().count()) + " HotelModel rows\n"
        s += str(RoomType.objects.filter().count()) + " RoomType rows\n"
        s += str(Room.objects.filter().count()) + " Room rows\n"
        s += str(RoomStatus.objects.filter().count()) + " RoomStatus row\n"
        s += str(RoomBooking.objects.filter().count()) + " RoomBooking rows\n"
        s += str(Billing.objects.filter().count()) + " Billing rows\n"
        return Response(data=s, status=status.HTTP_200_OK)
        

    @transaction.atomic
    def post(self, request):

        # Start Time
        start = time.time()

        #Deleting old data
        models = [CustomerUser, StaffUser, HotelModel, RoomType, 
        Room, RoomStatus, RoomBooking, Billing]
     
        for m in models:
            m.objects.all().delete()
        
        #Creating new data
     
        for _ in range(CUSTOMER_USER_NUMBER):
            CustomerUserFactory()

        for _ in range(HOTEL_NUMBER):
            HotelModelFactory()

        for _ in range(STAFF_USER_NUMBER):
            StaffUserFactory()
        
        for _ in range(ROOM_TYPE_NUMBER):
            RoomTypeFactory()

        for _ in range(ROOM_NUMBER):
            RoomFactory()
        
        for _ in range(ROOM_STATUS_NUMBER):
            RoomStatusFactory()

        for  _ in range(ROOM_BOOKING_NUMBER):
            RoomBookingFactory()
        
        for _ in range(BILLING_NUMBER):
            BillingFactory()
        
        # End Time
        end = time.time()
        exact_time = convert_time(end - start)
        print(exact_time)
        
        return Response("Data Generator processed.", status=status.HTTP_200_OK)
        