from django.urls import path
from django.conf.urls import url

from . import views
from .views import UserDetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('createEvent', views.createEvent, name='createEvent'),
    path('planNight', views.planNight, name='planNight'),
    path('search', views.search, name='search'),
    path('myNights', views.myNights, name='myNights'),
    path('myEvents', views.myEvents, name='myEvents'),

	url(r'^user/(?P<pk>\d+)/$', UserDetailView.as_view(), name='user_detail'),
]
