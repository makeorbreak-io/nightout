from django.db import models
from django.utils.timezone import now
import datetime

# Create your models here.

class Night(models.Model):
    events = models.CharField(max_length=140, blank=False)

class User(models.Model):
    name = models.CharField(max_length=30) 
    oauthkey = models.CharField(max_length=30)

    friends = models.ManyToManyField('self')

class Events(models.Model): 
    description = models.CharField(max_length=140, blank=False)
    image = models.FileField(upload_to='upload/')
    time = models.TimeField(max_length=30, default=now)
    date = models.DateField(max_length=30, default=now)
    local = models.CharField(max_length=30)
    private = models.BooleanField(default=False)
    price = models.IntegerField(default=0)

    users = models.ManyToManyField(User, related_name="events")

class Attending(models.Model):
    evento = models.ForeignKey(Events,
                               default='',
                               on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                             default='',
                             on_delete=models.CASCADE)
class Friends(models.Model):
    user1 = models.ForeignKey(User,
                              default='',
                              related_name='user1',
                              on_delete=models.CASCADE)
    user2 = models.ForeignKey(User,
                              default='',
                              related_name='user2',
                              on_delete=models.CASCADE)
