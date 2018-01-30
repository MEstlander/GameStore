from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('registration', views.registration, name='register'),
    path('registerGame', views.registerGame, name='registerGame')
]   
=======
]
>>>>>>> 093b7c12971540ca16dcfcd376af6cb0e0bb549d
