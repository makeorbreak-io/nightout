from django.db import models

# Create your models here.
# class Night(models.Model):

class Eventos(models.Model): 
    id = models.CharField(max_length=30, primary_key=True)
    descr = models.CharField(max_length=140, blank=False)
    date = models.DateTimeField(max_length=30)
    local = models.CharField(max_length=30)
    private = models.BooleanField(default=False)
    price = models.IntegerField(default=0)

class Users(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=30) 
    oauthkey = models.CharField(max_length=30)

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
