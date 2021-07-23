# Generated by Django 3.2.4 on 2021-06-28 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('RoomTypeCode', models.AutoField(primary_key=True, serialize=False)),
                ('RoomTypeName', models.CharField(default='', max_length=50)),
                ('UnitPrice', models.FloatField(default=0)),
                ('Description', models.CharField(default='', max_length=100)),
                ('VacancyAmount', models.IntegerField(default=0)),
                ('HotelCode', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Hotel.hotelmodel')),
            ],
        ),
        migrations.CreateModel(
            name='RoomStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RoomCode', models.IntegerField()),
                ('Date', models.DateField()),
                ('Status', models.IntegerField(choices=[(1, 'đang sử dụng'), (2, 'đang bảo trì'), (0, 'còn trống')])),
            ],
            options={
                'unique_together': {('RoomCode', 'Date')},
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('RoomCode', models.AutoField(primary_key=True, serialize=False)),
                ('RoomNumber', models.IntegerField(default=0)),
                ('RoomType', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Room.roomtype')),
            ],
        ),
    ]