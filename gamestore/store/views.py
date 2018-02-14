from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Game

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
    return render(request, 'store/library.html', {
        'title': 'GameStore - Library',
    })

# Helper methods


@login_required()
def registerGame(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = GameFrom()
    return render(request, 'store/game.html', {'form': form})

