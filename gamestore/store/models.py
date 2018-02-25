from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_developer = models.BooleanField("Developer", default=False)


class Game(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='thumbnails/', default='thumbnails/default.png')
    url = models.URLField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    developer = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    purchases = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    date = models.DateTimeField(auto_now_add=True)


class Highscores(models.Model):
    user = models.ForeignKey(User, related_name="hsuser", on_delete=models.CASCADE)
    game = models.ForeignKey(Game, related_name="hsgame", on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return (self.user.username, self.score)