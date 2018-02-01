from django.urls import path
from . import views

urlpatterns = [
    path('game/<game_name>/',views.play,name = 'play-view'),
]