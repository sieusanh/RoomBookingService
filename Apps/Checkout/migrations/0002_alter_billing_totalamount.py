# Generated by Django 3.2.5 on 2021-07-13 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='TotalAmount',
            field=models.IntegerField(),
        ),
    ]
