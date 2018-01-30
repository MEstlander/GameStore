from django.db import models
from django.contrib.auth.models import User
import store.models as x
# Create your models here.
class  Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    owned_games = models.ManyToManyField(x.Game,default=None,blank=True)

    #return username when the Profile is called
    def __str__(self):
        return str(self.user.username)
    