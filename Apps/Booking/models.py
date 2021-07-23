from django.db import models
from Apps.Room.models import RoomType
from Apps.User.models import CustomerUser

# Create your models here.
class RoomBooking(models.Model):
    RoomBookingCode = models.AutoField(primary_key=True)
    RoomTypeCode = models.ForeignKey(RoomType, to_field='RoomTypeCode', on_delete=models.DO_NOTHING)
    CustomerCode = models.ForeignKey(CustomerUser, to_field='CustomerCode', on_delete=models.DO_NOTHING)
    StartDate = models.DateField()
    EndDate = models.DateField()
    BookingDate = models.DateField()
    UnitPrice = models.IntegerField(default=0) # Unit price at the booking time
    Description = models.CharField(default='', max_length=100)
    STATUS_CHOICES = (
        (1, 'Đã xác nhận'),
        (2, 'Chưa xác nhận'),
    )
    Status = models.IntegerField(choices=STATUS_CHOICES)

