from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login
from .models import CustomerUser
from .serializers import UserRegistrySerializer, UserLoginSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions

# Create your views here.

# Customer User Registry View
class UserRegistryView(APIView):

    def get(self, request): 
        return Response('Userh Registry Site', status=status.HTTP_200_OK)

    def post(self, request):
        mydata = UserRegistrySerializer(data=request.data)
        if not mydata.is_valid():
            return Response('Nhập thông tin không hợp lệ', status=status.HTTP_400_BAD_REQUEST)
        # Username and ID_No must be unique
        if CustomerUser.objects.filter(Username=mydata.data['Username']).exists():
            return Response('Tên đăng nhập đã tồn tại', status=status.HTTP_400_BAD_REQUEST)
        if CustomerUser.objects.filter(ID_No=mydata.data['ID_No']).exists():
            return Response('Số Chứng Minh Nhân Dân đã được dùng để đăng ký tài khoản.', status=status.HTTP_400_BAD_REQUEST)

        # Create row in database
        cus_user = CustomerUser.objects.create(Name=mydata.data['Name'], Username=mydata.data['Username'], 
        Password=mydata.data['Password'], ID_No=mydata.data['ID_No'], 
        Address=mydata.data['Address'], PhoneNumber=mydata.data['PhoneNumber'], 
        Description=mydata.data['Description'], Email=mydata.data['Email'])
        
        return Response('Tạo tài khoản thành công', status=status.HTTP_200_OK)

class UserLoginView(APIView):

    def get(self, request):
        return Response(data="User Login Site", status=status.HTTP_200_OK)
    
    def post(self, request):
        mydata = UserLoginSerializer(data=request.data)
        if not mydata.is_valid():
            return Response('Nhập thông tin không hợp lệ', status=status.HTTP_400_BAD_REQUEST)
        
        username1 = mydata.data['Username']
        password1 = mydata.data['Password']
        # Check if any object has these two fields (Username, Password) exists in the database
        try:
            p = CustomerUser.objects.get(Username=username1, Password=password1)
        except ObjectDoesNotExist:
            return Response("Nhập sai Tên đăng nhập hoặc Mật khẩu", status=status.HTTP_400_BAD_REQUEST)
        
        my_user =  authenticate(request, email=username1, password=password1)
        print("username: " + username1 + " password: " + password1)
        if my_user is None:
            return Response("Nhập sai Tên đăng nhập hoặc Mật khẩu _ authen", status=status.HTTP_400_BAD_REQUEST)
        print("my_user data:" + str(my_user))    
        login(self.request, my_user)
        request.session['CustomerCode'] = p.CustomerCode
        
        return Response(data=user_info, status=status.HTTP_200_OK, content_type="text")
