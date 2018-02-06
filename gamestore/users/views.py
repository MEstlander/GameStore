from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, 'registration/base.html',{
        'title': 'GameStore - Registration',
        'content': 'registration/registration.html',
        'form': form
    })
    

def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password= password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/users/login/')
    form = AuthenticationForm()
    return render(request, 'registration/base.html',{
        'title': 'GameStore - Login',
        'content': 'registration/login.html',
        'form': form
    })
    

def log_out(request):
    logout(request)
    return redirect('/')

