from django.db import models
from django.utils.timezone import now
import datetime

# Create your models here.
# class Night(models.Model):

class Eventos(models.Model): 
    id = models.CharField(max_length=30, primary_key=True)
    description = models.CharField(max_length=140, blank=False)
    image = models.FileField(upload_to='upload/')
    time = models.DateTimeField(max_length=30, default=now())
    date = models.DateTimeField(max_length=30, default=now())
    local = models.CharField(max_length=30)
    private = models.BooleanField(default=False)
    price = models.IntegerField(default=0)

    users = models.ManyToManyField(User)

class Night(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    events = models.CharField(max_length=140, blank=False)

class User(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=30) 
    oauthkey = models.CharField(max_length=30)

    friends = models.ManyToManyField(User)

class Attending(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    evento = models.ForeignKey(Eventos,
                               on_delete=models.CASCADE)
    user = models.ForeignKey(Users,
                             on_delete=models.CASCADE)
class Friends(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    user1 = models.ForeignKey(Users,
                              related_name='user1',
                              on_delete=models.CASCADE)
    user2 = models.ForeignKey(Users,
                              related_name='user2',
                              on_delete=models.CASCADE)
