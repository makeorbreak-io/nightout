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

class Expenses(models.Model):

    EXPENSE_TYPES = (('FOOD', 'Food'),
                     ('DRINKS', 'Drinks'),
                     ('TRANSPORT', 'Transport'),)

    amount = models.IntegerField(blank=False)
    user = models.ForeignKey(User,
                             default='',
                             related_name='owes',
                             on_delete=models.CASCADE)
    expense_type = models.CharField(choices=EXPENSE_TYPES, max_length=30)

class Night(models.Model):
    title = models.CharField(max_length=140, blank=False)
    background_color = models.CharField(max_length=140)

    user = models.ManyToManyField(User, related_name="attending")
    events = models.ManyToManyField(Events, related_name="goes")
    expenses = models.ForeignKey(Expenses, on_delete=models.CASCADE, related_name="owes")
    # products = models.ManyToManyField(User, related_name="events")

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
