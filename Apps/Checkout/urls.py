from django.urls import path
from .views import BillingView

urlpatterns = [
    path('billing/', BillingView.as_view(), name='Billing'),
    
]