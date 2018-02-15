from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from store.models import Game
from django.shortcuts import get_object_or_404
# Create your views here.

@login_required
def play(request,game_name):
    game = get_object_or_404(Game, title=game_name)
    return render(request,"play_game/play.html", {'remote_server': game.url})

