# Generated by Django 2.0.4 on 2018-04-14 15:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0007_auto_20180414_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 14, 15, 4, 12, 596672, tzinfo=utc), max_length=30),
        ),
        migrations.AlterField(
            model_name='eventos',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 14, 15, 4, 12, 596630, tzinfo=utc), max_length=30),
        ),
    ]
