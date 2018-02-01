from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render
# Create your views here.


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration.html',{
        'title': 'GameStore - Registration',
        'header': 'registration',
        'form': form
    })
    

def login(request):
    form = AuthenticationForm()
    return render(request, 'registration/login.html',{
        'title': 'GameStore - Registration',
        'header': 'login',
        'form': form
    })
    


def logout(request):
    logout(request)

'''
def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration.html', {'form': form})


@login_required()
def registerGame(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = GameFrom()
    return render(request, 'registration/game.html', {'form': form})

'''