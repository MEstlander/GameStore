from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import User


def registration(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('/')
    else:
        user_form = UserCreationForm()
    return render(request, 'registration/register',{
        'form': user_form,
    })
