from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Game


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2', 'is_developer',)


class GameRegistrationForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('title', 'description', 'thumbnail', 'url', 'price',)
