from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('store/', views.store, name='store'),
    path('library/', views.library, name='library')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

