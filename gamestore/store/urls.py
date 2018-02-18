from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('account/login/', auth_views.LoginView.as_view(), name='login'),
    path('account/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('account/register/', views.registration, name="register"),
    path('store/', views.store, name='store'),
    path('game/registration/', views.register_game, name="register_game"),
    path('library/', views.library, name='library')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
