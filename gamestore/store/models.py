from django.db import models
import users.models as users


class Game(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='thumbnails/', default='thumbnails/default.png')
    url = models.URLField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    developer = models.ForeignKey(users.User, on_delete=models.DO_NOTHING, null=True, blank=True)
    purchases = models.IntegerField(default=0)

    def __str__(self):
        return self.title



    """
    class Category(models.Model):
        Category model for categories of games.
        id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=30, unique=True)

        def json(self):
            outputs data in json format
            json = {
                'id': self.id,
                'name': self.name
            }
            return json

        def __str__(self):
            return self.name

    class Game(models.Model):
        Games model for games
        id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=50, unique=True)
        price = models.FloatField(default=0)
        category = models.ForeignKey(Category, null=False, on_delete=models.CASCADE)
        url = models.URLField(unique = True)
        #add any data fields from Game model to json
        def json(self):
            outputs data in json format
            json = {
                'id': self.id,
                'name': self.name,
                'price': self.price,
                'category': self.category
            }
            return json

        def __str__(self):
            return self.name
    """

