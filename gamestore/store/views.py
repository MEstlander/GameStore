from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request, 'store/base.html', {
        'title': 'GameStore - Home',
        'content': 'store/homepage.html'
    })


def store(request):
    return render(request, 'store/base.html', {
        'title': 'GameStore - Store',
        'content': 'store/store.html'
    })


def library(request):
    return render(request, 'store/base.html', {
        'title': 'GameStore - Library',
        'content': 'store/library.html'
    })


@login_required()
def registerGame(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = GameFrom()
    return render(request, 'store/game.html', {'form': form})

