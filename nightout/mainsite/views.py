from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView

from  .forms import EventForm, NightForm
from .models import Events

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
            # event_data.local = form.cleaned_data['local']
            # event_data.private = form.cleaned_data['private']
            # event_data.price = form.cleaned_data['price']
            # event_data.creator = user.id

            event_data.save()
            # print(event_data.pk)
            event_data.pk = '0'
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

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
    def event_detail(request):
        redirect(index) 

class UserDetailView(DetailView):
    def user_detail(request):
        redirect(index)
