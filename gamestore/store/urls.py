from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('store/', views.store, name='store'),
    path('library/', views.library, name='library'),
    path('registration', views.registration, name='register'),
    path('registerGame', views.registerGame, name='registerGame')
]   

