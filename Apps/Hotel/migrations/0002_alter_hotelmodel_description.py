# Generated by Django 3.2.4 on 2021-06-29 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelmodel',
            name='Description',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
