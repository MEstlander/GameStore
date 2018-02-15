from django import forms
from .models import Game


class GameRegistrationForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('title', 'description', 'thumbnail', 'url', 'price',)