from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    title = 'Phastload'
    sitename = 'Main site'
    descr = 'Description'
    context = {'title' : title, 'sitename' : sitename, 'descr' : descr}

    return render(
        request,
        #'mainsite.html',
        'facebookLogin.html',
        context
    )
    #return HttpResponse("Hello, world.")
