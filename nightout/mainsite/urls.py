
from django.urls import path
from django.conf.urls import url
from django.conf import settings

from . import views
from .views import UserDetailView, EventsDetailView, NightsDetailView


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^login/$', views.custom_login, name='login'),
    path('postlogin', views.postlogin, name='postlogin'),
    path('createEvent', views.createEvent, name='createEvent'),
    path('planNight', views.planNight, name='planNight'),
    path('search', views.search, name='search'),
    path('myNights', views.myNights, name='myNights'),
    path('myEvents', views.myEvents, name='myEvents'),

    url(r'^user/(?P<pk>\d+)/$', UserDetailView.as_view(), name='user_detail'),
    url(r'^events/(?P<pk>\d+)$', EventsDetailView.as_view(), name='event_detail'),
    url(r'^nights/(?P<pk>\d+)$', NightsDetailView.as_view(), name='night_detail'),

    path('ajax/changeEventStatus', views.changeEventStatus, name='changeEventStatus'),
    path('ajax/search', views.search, name='search'),
    path('ajax/addUserNight', views.add_user_night, name='search'),

]

