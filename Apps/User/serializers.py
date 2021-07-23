from django.db import models
from rest_framework import serializers
from .models import CustomerUser

class UserRegistrySerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerUser
        fields = ("Name", "Username", "Password", "ID_No", "Address", "PhoneNumber", "Description", "Email")

class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerUser
        fields = ("Username", "Password")
        