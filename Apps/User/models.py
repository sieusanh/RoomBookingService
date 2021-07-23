
from django.db import models
from Apps.Hotel.models import HotelModel

# Create your models here.
class CustomerUser(models.Model):
    CustomerCode = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100, default='')
    Username = models.CharField(max_length=50, default='')
    Password = models.CharField(max_length=50, default='')
    ID_No = models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=30)
    Description = models.CharField(max_length=100, default='')
    Email = models.EmailField()

    def __str__(self):
        return str(self.CustomerCode)

class StaffUser(models.Model):
    StaffCode = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100, default='')
    Username = models.CharField(max_length=50, default='')
    Password = models.CharField(max_length=50, default='')
    HotelCode = models.ForeignKey(HotelModel, to_field='HotelCode', on_delete=models.DO_NOTHING)

    