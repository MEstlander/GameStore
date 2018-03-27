from django.http import HttpResponse, HttpResponseBadRequest
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from store.decorators import developer_required
from .forms import RegistrationForm, GameRegistrationForm
from .models import Game, Payment, Highscore
from hashlib import md5
import json


def homepage(request):
    all_games = Game.objects.all()
    featured_games = all_games[:3]
    return render(request, 'store/homepage.html', {
        'featured_games': featured_games
    })


def store(request):
    user = request.user
    all_games = Game.objects.all()
    if user.is_anonymous:
        return render(request, 'store/store.html', {
            'game_set': all_games
        })
    else:
        all_games = Game.objects.all()
        return render(request, 'store/store.html', context={
            'game_set': all_games,
        })


def library(request):
    user = request.user
    if user.is_anonymous:
        return render(request, 'store/library.html')
    else:
        purchased_games = Game.objects.filter(payment__user=user)
        developer_games = Game.objects.filter(developer=user)
        return render(request, 'store/library.html', {
            'purchased_games': purchased_games,
            'developer_games': developer_games
        })


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


@login_required()
def profile_view(request):
    user = request.user
    if user.is_anonymous:
        return redirect('homepage')
    else:
        payments = Payment.objects.filter(user=user)
        developer_games = Game.objects.filter(developer=user)
        total_revenue = 0
        for game in developer_games:
            total = game.price * game.purchases
            game.total = total
            total_revenue += total
        return render(request, 'store/profile.html', {
            'user': user,
            'payments': payments,
            'developer_games': developer_games,
            'total_revenue': total_revenue
        })


@login_required()
def payment(request, game_title):
    user = request.user
    game = Game.objects.get(title=game_title)
    if not Payment.objects.filter(user=user, game=game).exists() and not Game.objects.filter(id=game.id, developer=user).exists():
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
    else:
        return render(request, 'payment/ownership_message.html')

@login_required()
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

@login_required()
def payment_cancel(request):
    return render(request, 'payment/cancel.html')

def payment_error(request):
    return render(request, 'payment/error.html')


@developer_required()
def register_game(request):
    if request.method == 'POST':
        form = GameRegistrationForm(request.POST)
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
    user = request.user
    game = Game.objects.get(title=game_title)
    if Payment.objects.filter(user=user,game=game).exists() or Game.objects.filter(id=game.id, developer=user).exists():
        highscore = Highscore.objects.filter(game=game)
        top_5 = highscore[:5]
        if request.method == 'GET':
            #When you are redirected to an url it loads the game
            return render(request,"game/play.html", {
                'game_title': game.title,
                'remote_server': game.url,
                'top_highscores': top_5
            })
        elif request.method == 'POST':
            #TODO: add methods that add scores and saved games to db
            #remove current render when done just here so the server can be run
            score = request.POST.get('Score')
            save = Highscore.objects.create(user=request.user , game=game, score=score)
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
        return HttpResponseBadRequest('Access denied')

@login_required
def leaderboard(request, game_title):
    game = Game.objects.get(title=game_title)
    highscore = Highscore.objects.filter(game=game)
    return render(request, 'game/leaderboard.html', {
        'game_title': game.title,
        'highscores': highscore
    })