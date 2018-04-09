from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    title = 'Phastload'
    sitename = 'Hello World'
    descr = 'Description'
    context = {'title' : title, 'sitename' : sitename, 'descr' : descr}

    return render(
        request,
        'mainsite.html',
        context
    )
    #return HttpResponse("Hello, world.")
