from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_developer = models.BooleanField('developer status', default=False)
    # Add one to many field "Purchased games"

# Admin profile

# Gamer profile

# Developer profile
