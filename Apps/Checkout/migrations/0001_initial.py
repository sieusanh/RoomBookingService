# Generated by Django 3.2.4 on 2021-06-28 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('BillCode', models.AutoField(primary_key=True, serialize=False)),
                ('PaymentDate', models.DateField()),
                ('TotalAmount', models.FloatField()),
                ('RoomBookingCode', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Booking.roombooking')),
            ],
        ),
    ]
