from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
# Create your views here.

'''def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration.html', {'form': form})
'''


def registration(request):
    return render(request, 'registration/base.html', {
        'title': 'GameStore - Registration',
        'form': 'registration/registration.html'
    })


def login(request):
    return render(request, 'registration/base.html', {
        'title': 'GameStore - Login',
        'form': 'registration/login.html'
    })


def logout(request):
    pass