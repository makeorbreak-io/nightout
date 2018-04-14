from django.shortcuts import render
from django.http import HttpResponse

from  .forms import EventForm
from .models import *

from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def index(request):
    title = 'nightout'
    sitename = 'Hello World'
    descr = 'Description'
    context = {'title' : title, 'sitename' : sitename, 'descr' : descr}

    return render(request,
                  'mainsite.html',
                  context)

def createEvent(request):
    title = 'nightout'

    form = EventForm()

    context = {'title' : title, 'form' : form}

    return render(request, 'createEvent.html', context)

def mainpage(request):
    title = 'nightout'
    sitename = 'Hello World'

    if request.method == 'POST':
        form = EventForm(request.POST)

        if request.POST['eventName']:
            print(request.POST)
            evnt = Eventos(date=request.POST['date'], local=request.POST['local'])
            evnt.save()

    context = {'title' : title, 'sitename' : sitename}

    return render(
        request,
        'feed.html',
        context
    )
    #return HttpResponse("Hello, world.")
