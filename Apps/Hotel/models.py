from django.db import models

# Create your models here.
class HotelModel(models.Model):
    HotelCode = models.AutoField(primary_key=True)
    HotelName = models.CharField(default='', max_length=50)
    StarType = models.IntegerField(default=0, null=True, blank=True)
    HouseNumber = models.IntegerField(default=0)
    Street = models.CharField(default='', max_length=50)
    District = models.CharField(default='', max_length=50)
    City = models.CharField(default='', max_length=50)
    AveragePrice = models.IntegerField(default=0, null=True, blank=True)
    Description = models.CharField(default='', max_length=100)

    def __str__(self):
        return str(self.HotelCode)
