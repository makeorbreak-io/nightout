from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView

from  .forms import EventForm, NightForm
from .models import Events, User
from social_django.models import UserSocialAuth

from django.contrib.auth.decorators import login_required
from django.utils import timezone

import random
import itertools

def postlogin(request):
    return redirect(index)

def index(request):
    title = 'nightout'
    sitename = 'Hello World'
    user = request.user

    if not user.is_authenticated:
        return redirect('login')

    context = {'title' : title, 'sitename' : sitename, 'user':user}

    return render(
        request,
        'mainsite.html',
        context
    )
    #return HttpResponse("Hello, world.")

def createEvent(request):
    title = 'nightout'

    context = {'title' : title, }

    if request.method == 'POST':
        form = EventForm(request.POST)
        print(form.errors)

        if form.is_valid():
            event_data = Events()
            event_data.description = form.cleaned_data['description']
            # event_data.image = form.cleaned_data['image']
            event_data.time = form.cleaned_data['time']
            event_data.date = form.cleaned_data['date']
            event_data.local = form.cleaned_data['local']
            event_data.private = form.cleaned_data['private']
            event_data.price = form.cleaned_data['price']

            event_data.creator = User.objects.get(pk=request.user.id)

            event_data.save()
            # event_data.pk = '0'

            return HttpResponseRedirect('events/' + event_data.pk)
        else:
            context['error'] = 'Not valid'
            return render(request, 'mainsite.html', context)
    else:
        form = EventForm()
        context['form'] = form 

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

class EventsDetailView(DetailView):
    template_name='events_detail.html'
    queryset = Events.objects.all()

    def event_detail(request):
        title = 'nightout'
        context = {'title' : title}

        return context

class UserDetailView(DetailView):
    def user_detail(request):
        redirect(index)
