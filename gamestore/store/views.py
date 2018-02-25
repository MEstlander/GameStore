from django.http import HttpResponse, HttpResponseBadRequest
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from store.decorators import developer_required
from .forms import RegistrationForm, GameRegistrationForm
from .models import User, Game, Payment, Highscores
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

def profile_view(request):
    user = request.user
    if user.is_anonymous:
        return redirect('homepage')
    else:
        payments = Payment.objects.filter(user=user)
        developer_games = Game.objects.filter(developer=user)
        return render(request, 'store/profile.html', {
            'user': user,
            'developer_games': developer_games
        })


def homepage(request):
    return render(request, 'store/homepage.html')


def store(request):
    user = request.user
    all_games = Game.objects.all()
    if user.is_anonymous:
        return render(request, 'store/store.html', {
            'game_set': all_games
        })
    else:
        all_games = Game.objects.all()
        purchased_games = Game.objects.filter(payment__user=user)
        inventory = Game.objects.filter(developer=user)
        game_set = all_games.exclude(id__in=[o.id for o in purchased_games])
        return render(request, 'store/store.html', context={
            'game_set': game_set,
        })


def library(request):
    user = request.user
    if user.is_anonymous:
        return render(request, 'store/library.html', context={
            'game_set': [],
        })
    else:
        purchased_games = Game.objects.filter(payment__user=user)
        inventory = Game.objects.filter(developer=user)
        return render(request, 'store/library.html', {
            'purchased_games': purchased_games,
            'inventory': inventory,
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
        checksum = request.GET.get('checksum', '')
        pid = request.GET.get('pid', '')
        ref = request.GET.get('ref', '')
        result = request.GET.get('result', '')
        secret_key = 'ea22e857acbfe3653cad46f2d70b99d5'
        checksumstr = "pid={}&ref={}&result={}&token={}".format(pid, ref, result, secret_key)
        m = md5(checksumstr.encode('ascii'))
        calc_checksum = m.hexdigest()
        if checksum == calc_checksum:
            user = request.user
            game = Game.objects.get(id=pid)
            if not Payment.objects.filter(user=user, game=game).exists():
                new_payment = Payment(
                    user=user,
                    game=game,
                    amount=game.price
                )
                new_payment.save()
            Game.objects.filter(id=game.id).update(purchases=game.purchases+1)
            return render(request, 'payment/success.html', {
                'pid': pid,
                'ref': ref,
            })

    return HttpResponseBadRequest('Invalid checksum')


def payment_cancel(request):
    return render(request, 'payment/cancel.html')

def payment_error(request):
    return render(request, 'payment/error.html')


@developer_required()
def register_game(request):
    if request.method == 'POST':
        form = GameRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.developer = request.user
            f.save()
            return redirect('store')
    else:
        form = GameRegistrationForm()

    return render(request, 'game/register_game.html', {'form': form})


@login_required
def play(request, game_title):
    game = get_object_or_404(Game, title=game_title)
    highscores = game.hsgame.all()
    if request.method == 'GET':
        #When you are redirected to an url it loads the game
        return render(request,"game/play.html", {'remote_server': game.url,'highscores': highscores})

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