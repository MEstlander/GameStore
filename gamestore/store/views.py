from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from store.decorators import developer_required
from .forms import RegistrationForm, GameRegistrationForm
from .models import Game


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('homepage')
    else:
        form = RegistrationForm
    return render(request, 'registration/register.html', {
        'form': form
    })


def homepage(request):
    return render(request, 'store/homepage.html', {
        'title': 'GameStore - Home'
    })


def store(request):
    game_set = Game.objects.all()
    return render(request, 'store/store.html', context = {
        'game_set': game_set,
        'title': 'GameStore - Store'
    })



def library(request):
    purchased_games = Game.objects.all()
    return render(request, 'store/library.html', {
        'purchased_games': purchased_games,
        'title': 'GameStore - Library',
    })


@developer_required()
def register_game(request):
    if request.method == 'POST':
        form = GameRegistrationForm(request.POST, request.FILES)
        if form.is_valid:
            f = form.save(commit=False)
            f.developer = request.user
            f.save()
            return redirect('homepage')
    else:
        form = GameRegistrationForm()

    return render(request, 'store/register_game.html', {'form': form})

