from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from store.decorators import developer_required
from .forms import RegistrationForm, GameRegistrationForm
from .models import Game, Payment, Highscores
from hashlib import md5
import json

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
    return render(request, 'store/store.html', context={
        'game_set': game_set,
        'title': 'GameStore - Store'
    })


def payment(request, game_title):
    game = Game.objects.get(title=game_title)
    pid = str(game.pk)
    sid = '43124917'
    amount = game.price
    success_url = request.build_absolute_uri(reverse('payment_success'))
    print(success_url)
    cancel_url = request.build_absolute_uri(reverse('payment_cancel'))
    error_url = request.build_absolute_uri(reverse('payment_error'))
    secret_key = 'ea22e857acbfe3653cad46f2d70b99d5'
    checksumstr = "pid={}&sid={}&amount={}&token={}".format(pid, sid, amount, secret_key)
    m = md5(checksumstr.encode("ascii"))
    checksum = m.hexdigest()
    payment_details = {
        'pid': pid,
        'sid': sid,
        'amount': amount,
        'success_url': success_url,
        'cancel_url': cancel_url,
        'error_url': error_url,
        'checksum': checksum
    }
    return render(request, 'payment/verification.html', {'payment_details': payment_details})

def payment_success(request):
    if request.method == 'GET':
        pid = request.GET.get('pid')
        new_payment = Payment(
            user=request.user,
            game=Game.objects.get(id=pid)
        )
        new_payment.save()
    else:
        HttpResponse('Only GET allowed')
    return render(request, 'payment/success.html')

def payment_cancel(request):
    return render(request, 'payment/cancel.html')

def payment_error(request):
    return render(request, 'payment/error.html')


def library(request):
    purchased_games = Game.objects.filter(payment__user=request.user)
    inventory = Game.objects.filter(developer=request.user)
    return render(request, 'store/library.html', {
        'purchased_games': purchased_games,
        'inventory': inventory,
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

    return render(request, 'game/register_game.html', {'form': form})


@login_required
def play(request, game_title):
    game = get_object_or_404(Game, title=game_title)

    if request.method == 'GET':
        #When you are redirected to an url it loads the game
        return render(request,"game/play.html", {'remote_server': game.url})

    elif request.method == 'POST':
        #TODO: add methods that add scores and saved games to db
        #remove current render when done just here so the server can be run
        score = request.POST.get('Score')
        print(score)
        print("\n HELLOOOOOO \n")
        save = Highscores.objects.create(user=request.user , game=game, score=score)
        #save.save()
        reposnse_data = {}
        reposnse_data['result'] = 'Score saved successfully'
        reposnse_data['score'] = score
        reposnse_data['user'] = request.user.username
        return HttpResponse(
            json.dumps(reposnse_data),
            content_type="application/json"
        )

    else:
        #If request method is not get or post it's invalid
        return HttpResponse(405, content="Invalid method")

        