from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DetailView

from  .forms import EventForm, NightForm
from .models import *

from django.contrib.auth.decorators import login_required
from django.utils import timezone

import random
import itertools

def index(request):
    title = 'nightout'
    sitename = 'Hello World'

    if not user.is_authenticated:
        return redirect('login')

    userEvents = feedEvents(user)

    context = {'title' : title, 'sitename' : sitename, 'user':user, 'items':userEvents}
    
    return render(
        request,
        'mainsite.html',
        context
    )
    #return HttpResponse("Hello, world.")

def createEvent(request):
    title = 'nightout'

    form = EventForm()

    context = {'title' : title, 'form' : form}

    return render(request, 'createEvent.html', context)

def planNight(request):
    title = 'nightout'

    form = NightForm()

    context = {'title' : title, 'form' : form}

    return render(request, 'planNight.html', context)

def search(request):
    redirect(index)

def myNights(request):
    redirect(index)

def myEvents(request):
    redirect(index)

class UserDetailView(DetailView):
    def user_detail(request):
        redirect(index) 

def feedEvents(user):
    now = timezone.now()

    userQ = User.objects.get(pk=user.id)
    attending = userQ.events.filter(date__gte=now).order_by('date')[:10]
    notAttending = Events.objects.exclude (users__id = user.id, date__lt=now).order_by('date')[:10]
    feedEvents = list(itertools.chain(attending, notAttending))
    eventsShuffled = sorted(feedEvents, key=lambda x: random.random())[:10]
    
    results={}
    for event in eventsShuffled:
        eventDict={}
        if event in attending:
            eventDict['status'] = 'Going'
        else:
            eventDict['status']= 'Not Going'
        
        goingTo = event.users.values_list('id',flat=True)
        f = userQ.friends.filter(id__in = goingTo)        
        
        eventDict['friends'] = f
        results[event] = eventDict

    return results
    #Only upcoming events (E se forem eventos a decorrer?)