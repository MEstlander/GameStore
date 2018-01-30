from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
<<<<<<< HEAD
from .forms import GameFrom
=======

@login_required()
def inventory(request):
    return HttpResponse("Hello there is nothing here")
>>>>>>> 093b7c12971540ca16dcfcd376af6cb0e0bb549d

@login_required()
def index(request):
    return HttpResponse("Hello, world. You're at the store index.")
<<<<<<< HEAD

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def registerGame(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = GameFrom()
    return render(request, 'registration/game.html', {'form': form})
=======
>>>>>>> 093b7c12971540ca16dcfcd376af6cb0e0bb549d
