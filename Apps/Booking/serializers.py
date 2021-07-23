from django.db import models
from rest_framework import serializers
from .models import RoomBooking

class RoomBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomBooking
        fields = ('StartDate', 'EndDate', 'Description', 'Status')
    