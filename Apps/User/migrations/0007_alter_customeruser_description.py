# Generated by Django 3.2.5 on 2021-07-12 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_alter_customeruser_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='Description',
            field=models.CharField(default='', max_length=100),
        ),
    ]
