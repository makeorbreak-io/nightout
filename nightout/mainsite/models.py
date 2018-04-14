from django.db import models
from django.utils.timezone import now
import datetime

from social_django.models import UserSocialAuth as User

# Create your models here.
# class Night(models.Model):

class Night(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    events = models.CharField(max_length=140, blank=False)

class Events(models.Model): 
    id = models.CharField(max_length=30, primary_key=True)
    description = models.CharField(max_length=140, blank=False)
    # image = models.FileField(upload_to='upload/', default='', blank=True)
    time = models.TimeField(max_length=30, default=now)
    date = models.DateField(max_length=30, default=now)
    local = models.CharField(max_length=30)
    private = models.BooleanField(default=False)
    price = models.IntegerField(default=0)
    creator = models.ForeignKey(User,
                                default='',
                                related_name='creator',
                                on_delete=models.CASCADE)

    users = models.ManyToManyField(User)

class Attending(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    evento = models.ForeignKey(Events,
                               default='',
                               on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                             default='',
                             on_delete=models.CASCADE)
class Friends(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    user1 = models.ForeignKey(User,
                              default='',
                              related_name='user1',
                              on_delete=models.CASCADE)
    user2 = models.ForeignKey(User,
                              default='',
                              related_name='user2',
                              on_delete=models.CASCADE)
