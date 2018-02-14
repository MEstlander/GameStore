from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from store.models import Game
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    owned_games = models.ManyToManyField(Game,default=None,blank=True)
    is_developer = models.BooleanField(default=False) #player if false, developer if true

    @property
    def dev(self):
        return Profile.is_developer
    #return username when the Profile is called
    def __str__(self):
        return str(self.user.username)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
