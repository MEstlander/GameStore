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
    path('account/profile/', views.profile_view, name="profile_view"),
    path('game/registration/', views.register_game, name="register_game"),
    path('store/', views.store, name='store'),
    path('library/', views.library, name='library'),
    path('play/<game_title>/', views.play, name='play'),
    path('purchase/<game_title>', views.payment, name='payment'),
    path('payment/success/', views.payment_success, name='payment_success'),
    path('payment/cancel/', views.payment_cancel, name='payment_cancel'),
    path('payment/error/', views.payment_error, name='payment_error')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
