from django.db import models
from Apps.Hotel.models import HotelModel

# Create your models here.
class RoomType(models.Model):
    RoomTypeCode = models.AutoField(primary_key=True)
    RoomTypeName = models.CharField(max_length=50, default='')
    HotelCode = models.ForeignKey(HotelModel, to_field='HotelCode', on_delete=models.DO_NOTHING)
    UnitPrice = models.IntegerField(default=0)
    Description = models.CharField(default='', max_length=100)
    VacancyAmount = models.IntegerField(default=0)

class Room(models.Model):
    RoomCode = models.AutoField(primary_key=True)
    RoomType = models.ForeignKey(RoomType, to_field='RoomTypeCode', on_delete=models.DO_NOTHING)
    RoomNumber = models.IntegerField(default=0)

class RoomStatus(models.Model):
    RoomCode = models.ForeignKey(Room, to_field='RoomCode', on_delete=models.DO_NOTHING)
    Date = models.DateField()
    STATUS_CHOICES = (
        (1, 'đang sử dụng'),
        (2, 'đang bảo trì'),
        (0, 'còn trống'),
    )
    Status = models.IntegerField(choices=STATUS_CHOICES)

    class Meta:
        unique_together = (('RoomCode', 'Date'),)
