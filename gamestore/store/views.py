from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .forms import GameFrom

@login_required()
def index(request):
    return HttpResponse("Hello, world. You're at the store index.")

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
