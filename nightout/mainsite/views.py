from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
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

    context = {'title' : title, 'sitename' : sitename, 'user':user ,'items' : feedEvents(user)}

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
            event_data.title = form.cleaned_data['title']
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

            return HttpResponseRedirect('events/' + str(event_data.pk))
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

    user = request.user
    context = {'events': user.events.all()}
    return render(request, 'my_events.html', context)


class EventsDetailView(DetailView):
    template_name='events_detail.html'
    model = Events

    def get_context_data(self, **kwargs):
        context = super(EventsDetailView, self).get_context_data(**kwargs)
        eventID = self.kwargs['pk']
        event= Events.objects.get(pk=eventID)
        user = self.request.user
        context['friends'] = getFriends(user,event)
        return context


class UserDetailView(DetailView):
    template_name='user_detail.html'
    model = User

def getFriends(user,event):
    userQ = User.objects.get(pk=user.id)
    goingTo = event.users.values_list('id',flat=True)
    f = userQ.friends.filter(id__in = goingTo)
    return f

def feedEvents(user):
    now = timezone.now()

    userQ = User.objects.get(pk=user.id)
    attending = userQ.events.all().order_by('date')[:10]
    notAttending = Events.objects.exclude (users__id = user.id, date__lt=now).order_by('date')[:10]
    feedEvents = list(itertools.chain(attending, notAttending))
    eventsShuffled = sorted(feedEvents, key=lambda x: random.random())[:10]

    results={}
    for event in eventsShuffled:
        eventList = []
        if event in attending:
            eventList.append('Going')
        else:
            eventList.append('Not Going')

        f = getFriends(user,event)

        eventList.append(f)
        results[event] = eventList

    return results
    #Only upcoming events (E se forem eventos a decorrer?)


def changeEventStatus(request):

    if request.method == "POST":
        event = Events.objects.get(pk=request.POST.get('EventId'))
        if request.POST.get('value') == "1":
            event.users.remove(User.objects.get(pk=request.user.id))
        else:
            event.users.add(User.objects.get(pk=request.user.id))

        event.save()
        return HttpResponse("Success")

def search(request):

    if request.method == "POST":

        search_string = request.POST.get('search')
        users = User.objects.filter(first_name__icontains=search_string)
        print(users)
        users = serializers.serialize('json', users)
        return JsonResponse(users,safe=False)
