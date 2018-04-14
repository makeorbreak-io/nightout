from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import auth, messages
from django.contrib.auth import login, authenticate, update_session_auth_hash, logout as auth_logout
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required

from social_django.models import UserSocialAuth

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

def home(request):
    user = request.user
    if user.is_authenticated:
        try:
            facebook_login = user.social_auth.get(provider='facebook')
        except UserSocialAuth.DoesNotExist:
            facebook_login = None
    else:
        facebook_login = None
    
    context = {'user' : user, 'facebook_login' : facebook_login}

    #can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())
    return render(request, 'home.html', context)

@login_required
def settings(request):
    user = request.user

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'settings.html', {
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })

@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'password.html', {'form': form})
