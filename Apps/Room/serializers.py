from rest_framework import serializers
from django.db import models
from .models import RoomType, Room, RoomStatus

class RoomTypeChooseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ('RoomTypeCode')

class RoomChooseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('RoomCode')

class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomStatus
        fields = ('Date')

class RoomStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomStatus
        fields = ('RoomCode', 'Date', 'Status')