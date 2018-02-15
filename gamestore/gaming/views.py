from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from store.models import Game
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponse
# Create your views here.

@login_required
def play(request,game_name):
    game = get_object_or_404(Game, title=game_name)
    
    if request.method == 'GET':
        #When you are redirected to an url it loads the game
        return render(request,"play_game/play.html", {'remote_server': game.url})

    elif request.method == 'POST':
        #TODO: add methods that add scores and saved games to db
        #remove current render when done just here so the server can be run
        return render(request,"play_game/play.html", {'remote_server': game.url})


    else: 
        #If request method is not get or post it's invalid
        return HttpResponse(405, content="Invalid mehtod")

