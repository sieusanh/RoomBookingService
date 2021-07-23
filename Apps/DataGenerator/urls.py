
from django.urls import path
from .views import DataGeneratorView

urlpatterns = [
    path('', DataGeneratorView.as_view()),
]
