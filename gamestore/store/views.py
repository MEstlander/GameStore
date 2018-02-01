from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .forms import GameFrom


def homepage(request):
    return render(request, 'base.html', {
        'title': 'GameStore - Home',
        'content': 'homepage/content.html'
    })


def store(request):
    return render(request, 'base.html', {
        'title': 'GameStore - Store',
        'content': 'store/content.html'
    })


def library(request):
    return render(request, 'base.html', {
        'title': 'GameStore - Library',
        'content': 'library/content.html'
    })


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required()
def registerGame(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = GameFrom()
    return render(request, 'registration/game.html', {'form': form})

