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
    return render(request, 'registration/registration.html',{
        'title': 'GameStore - Registration',
        'header': 'registration',
        'form': form
    })
    

def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password= password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/users/login/')
    form = AuthenticationForm()
    return render(request, 'registration/login.html',{
        'title': 'GameStore - Login',
        'header': 'login',
        'form': form
    })
    

def log_out(request):
    logout(request)
    return redirect('/')

