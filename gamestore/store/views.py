from django.shortcuts import render


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


@login_required()
def registerGame(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = GameFrom()
    return render(request, 'developer/game.html', {'form': form})

