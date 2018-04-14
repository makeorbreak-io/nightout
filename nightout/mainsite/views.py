from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DetailView

from  .forms import EventForm, NightForm
from .models import *

from django.contrib.auth.decorators import login_required


def index(request):
    title = 'nightout'
    sitename = 'Hello World'

    context = {'title' : title, 'sitename' : sitename}

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

def myNights(request):

def myEvents(request):

class UserDetailView(DetailView):
    def user_detail(request):