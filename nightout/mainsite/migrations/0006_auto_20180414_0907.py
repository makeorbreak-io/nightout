# Generated by Django 2.0.4 on 2018-04-14 09:07

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0005_auto_20180414_0145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Night',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event', to='mainsite.Users')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='mainsite.Users')),
            ],
        ),
        migrations.AlterField(
            model_name='eventos',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 14, 9, 7, 2, 541168, tzinfo=utc), max_length=30),
        ),
        migrations.AlterField(
            model_name='eventos',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 14, 9, 7, 2, 541133, tzinfo=utc), max_length=30),
        ),
    ]
