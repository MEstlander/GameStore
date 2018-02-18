from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_developer = models.BooleanField("Developer", default=False)


class Game(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='thumbnails/', default='thumbnails/default.png')
    url = models.URLField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    developer = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    purchases = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class PurchasedGames(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    game = models.ForeignKey(Game, on_delete=models.DO_NOTHING)