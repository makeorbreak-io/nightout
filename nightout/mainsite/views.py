from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def index(request):
    title = 'nightout'
    sitename = 'Hello World'
    descr = 'Description'
    context = {'title' : title, 'sitename' : sitename, 'descr' : descr}

    return render(
        request,
        'mainsite.html',
        context
    )
    #return HttpResponse("Hello, world.")

