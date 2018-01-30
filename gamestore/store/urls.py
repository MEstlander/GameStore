from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration', views.registration, name='register'),
    path('registerGame', views.registerGame, name='registerGame')
]   