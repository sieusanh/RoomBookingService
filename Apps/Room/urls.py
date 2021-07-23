from django.urls import path
from .views import HotelSearchView, RoomTypeSearchView, RoomSearchView, RoomStatusSearchView, RoomStatusUpdateView

urlpatterns = [
    path('hotel/', HotelSearchView.as_view(), name='Room_HotelSearch'),
    path('roomtype/', RoomTypeSearchView.as_view(), name='RoomType'),
    path('room/', RoomSearchView.as_view(), name='Room'),
    path('roomstatus_search/', RoomStatusSearchView.as_view(), name='RoomStatusSearch'),
    path('roomstatus_update/', RoomStatusUpdateView.as_view())
]