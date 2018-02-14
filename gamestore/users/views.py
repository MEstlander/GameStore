from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import Profile
from common.utils import is_dev
import textwrap

from django.http import HttpResponse
from django.views.generic.base import View

def registration(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/')
    else:
        user_form = UserCreationForm()
        profile_form = ProfileForm()
    return render(request, 'registration/base.html',{
        'title': 'GameStore - Registration',
        'content': 'registration/registration.html',
        'user_form': user_form,
        'profile_form': profile_form,
    })


def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password= password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/users/login/')
    form = AuthenticationForm()
    return render(request, 'registration/base.html',{
        'title': 'GameStore - Login',
        'content': 'registration/login.html',
        'form': form
    })



def log_out(request):
    logout(request)
    return redirect('/')


@login_required() #just for testing if we can restrict websites to devs
@user_passes_test(is_dev)
def test(request):
    response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Greetings to the world</title>
            </head>
            <body>
                <h1>Greetings to the world</h1>
                <p>Hello, world!</p>
            </body>
            </html>
        ''')
    return HttpResponse(response_text)
