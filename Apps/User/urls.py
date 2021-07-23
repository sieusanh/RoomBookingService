
from django.urls import path
from .views import UserRegistryView, UserLoginView

urlpatterns = [
    path('registry/', UserRegistryView.as_view()),
    path('login/', UserLoginView.as_view()),
]
