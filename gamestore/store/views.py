from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

@login_required()
def inventory(request):
    return HttpResponse("Hello there is nothing here")

@login_required()
def index(request):
    return HttpResponse("Hello, world. You're at the store index.")
