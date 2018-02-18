from django.contrib import admin
from .models import User, Game
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Game)
