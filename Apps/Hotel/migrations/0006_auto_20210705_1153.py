# Generated by Django 3.2.4 on 2021-07-05 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0005_auto_20210705_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelmodel',
            name='AveragePrice',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='hotelmodel',
            name='StarType',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]