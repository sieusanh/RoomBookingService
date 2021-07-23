from django.db import models
from rest_framework import serializers
from .models import HotelModel

class AddNewHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelModel
        fields = ('HotelName', 'StarType', 'HouseNumber', 'Street', 
        'District', 'City', 'AveragePrice', 'Description')

        
class HotelSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelModel
        fields = ('StarType', 'City', 'AveragePrice')
        
        '''
        CRITERIA_CHOICES = (
            ('AveragePrice', 'City'),
            ('StarType', 'City'),
            ('City'),
        )
        fields = serializers.ChoiceField(choices=CRITERIA_CHOICES)
        '''
        #fields = '__all__'

class HotelChooseSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelModel
        fields = ('HotelCode')