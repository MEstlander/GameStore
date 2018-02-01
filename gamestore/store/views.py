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

