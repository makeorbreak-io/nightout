# Generated by Django 2.0.4 on 2018-04-14 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0006_remove_events_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='creator',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='mainsite.User'),
        ),
    ]
