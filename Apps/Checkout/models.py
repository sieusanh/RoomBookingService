from Apps.Booking.models import RoomBooking
from django.db import models
from Apps.Booking.models import RoomBooking

# Create your models here.
class Billing(models.Model):
    BillCode = models.AutoField(primary_key=True)
    PaymentDate = models.DateField()
    TotalAmount = models.IntegerField()
    RoomBookingCode = models.ForeignKey(RoomBooking, to_field='RoomBookingCode', on_delete=models.DO_NOTHING)

