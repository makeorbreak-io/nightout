from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('mainpage', views.mainpage, name='mainpage'),
    path('createEvent', views.createEvent, name='createEvent')
]

