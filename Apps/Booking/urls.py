from django.urls import path
from .views import RoomBookingView

urlpatterns = [
    path('hotel/', RoomBookingView.as_view(), name='RoomBooking'),
    
]