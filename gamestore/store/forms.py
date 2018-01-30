from django import forms
from .models import Game

class GameFrom(forms.ModelForm):

    class Meta:
        model = Game
        fields = ('name', 'price', 'category', 'url',)