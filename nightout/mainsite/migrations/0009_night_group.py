# Generated by Django 2.0.4 on 2018-04-15 02:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0008_auto_20180415_0133'),
    ]

    operations = [
        migrations.AddField(
            model_name='night',
            name='group',
            field=models.ManyToManyField(related_name='group', to=settings.AUTH_USER_MODEL),
        ),
    ]
