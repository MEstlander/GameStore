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
