# Generated by Django 4.0.4 on 2022-05-06 13:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0004_auto_20220412_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine',
            name='num',
        ),
        migrations.AddField(
            model_name='machine',
            name='mach',
            field=models.CharField(choices=[('PC', 'PC - Run windows '), ('Mac ', 'MAc - Run MacOS '), ('Serveur ', 'Serveur - Simple Server to deploy virtual machines '), ('Switch ', 'Switch - To maintains and connect servers ')], default='PC', max_length=32),
        ),
        migrations.AddField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2022, 5, 6, 13, 13, 10, 345854)),
        ),
    ]