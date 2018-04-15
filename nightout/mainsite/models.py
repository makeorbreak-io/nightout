from django.db import models
from django.utils.timezone import now
import datetime

from django.contrib.auth.models import AbstractUser

from social_django.models import UserSocialAuth
# Create your models here.
# class Night(models.Model):

class User(AbstractUser):
    friends = models.ManyToManyField('self', related_name='friends')
    picture  = models.CharField(max_length=500, default='', blank=True)
    phone_number  = models.CharField(max_length=500, default='', blank=True)

    comDividendo = models.ManyToManyField('self', through='Dividendos', symmetrical=False)

class Events(models.Model): 
    title = models.CharField(max_length=30, blank=False, null=False, default='')
    description = models.CharField(max_length=140, blank=False)
    # image = models.FileField(upload_to='upload/', default='', blank=True)
    time = models.TimeField(max_length=30, default=now)
    date = models.DateField(max_length=30, default=now)
    local = models.CharField(max_length=1000)
    private = models.BooleanField(default=False)
    price = models.IntegerField(default=0)
    background_color = models.CharField(max_length=140)
    creator = models.ForeignKey(User,
                                default='',
                                related_name='creator',
                                on_delete=models.CASCADE)

    users = models.ManyToManyField(User, related_name="events")

class Night(models.Model):
    title = models.CharField(max_length=140, blank=False)
    background_color = models.CharField(max_length=140)

    user = models.ManyToManyField(User, related_name="attending")
    events = models.ManyToManyField(Events, related_name="goes")
    # expenses = models.ManyToManyField(Expenses, related_name="owes")
    # products = models.ManyToManyField(User, related_name="events")

class Expenses(models.Model):

    EXPENSE_TYPES = (('FOOD', 'Food'),
                     ('DRINKS', 'Drinks'),
                     ('TRANSPORT', 'Transport'),)

    amount = models.IntegerField(blank=False)
   
    expense_type = models.CharField(choices=EXPENSE_TYPES, max_length=30)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses_bought')
    night = models.ForeignKey(Night, on_delete=models.CASCADE, related_name='expenses')
    debtors = models.ManyToManyField(User, related_name="expenses")


class Dividendos(models.Model):
  aDever = models.ForeignKey(User, related_name = 'dividendos_aDever' , on_delete=models.CASCADE)
  cobrador = models.ForeignKey(User, related_name = 'dividendos_aCobrar',  on_delete=models.CASCADE)
  value = models.FloatField(default='')
  night = models.ForeignKey(Night, related_name = 'dividendos',on_delete=models.CASCADE)

class Attending(models.Model):
    evento = models.ForeignKey(Events,
                               default='',
                               on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                             default='',
                             related_name='attending_user',
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
