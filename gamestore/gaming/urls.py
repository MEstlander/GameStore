from django.urls import path
from . import views

urlpatterns = [
    path('game/<gameid>/',views.play,name = 'play-view'),
]