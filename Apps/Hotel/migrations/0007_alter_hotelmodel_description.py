# Generated by Django 3.2.5 on 2021-07-12 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0006_auto_20210705_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelmodel',
            name='Description',
            field=models.CharField(default='', max_length=100),
        ),
    ]
