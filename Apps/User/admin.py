from django.contrib import admin
from .models import StaffUser, CustomerUser

# Register your models here.
admin.site.register(StaffUser),
admin.site.register(CustomerUser),
