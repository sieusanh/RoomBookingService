# Generated by Django 3.2.4 on 2021-06-28 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='ID_No',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customeruser',
            name='PhoneNumber',
            field=models.IntegerField(max_length=30),
        ),
    ]