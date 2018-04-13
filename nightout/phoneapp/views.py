from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    title = 'Phone nightout'
    sitename = 'Phone Main site'
    descr = 'Phone Description'
    context = {'title' : title, 'sitename' : sitename, 'descr' : descr}

    return render(
        request,
        'mainsite.html',
        context
    )

