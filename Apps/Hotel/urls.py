from django.urls import path
from .views import HotelSearchView, AddNewHotelView

urlpatterns = [
    path('search/', HotelSearchView.as_view()),
    path('add/', AddNewHotelView.as_view()),
    
]