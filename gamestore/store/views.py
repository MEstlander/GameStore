from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.decorators import developer_required
from .models import Game
from .forms import GameRegistrationForm

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

