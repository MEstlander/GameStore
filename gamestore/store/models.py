"""Barebones structure for models currently has name and id only
TODO: add in rest of required fields"""
from django.db import models


class Category(models.Model):
    """Category model for categories of games."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)

    def json(self):
        """outputs data in json format"""
        json = {
            'id': self.id,
            'name': self.name
        }
        return json

    def __str__(self):
        return self.name


class Game(models.Model):
    """Games model for games"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    price = models.FloatField(default=0)
    category = models.ForeignKey(Category, null=False, on_delete=models.CASCADE)

    #add any data fields from Game model to json
    def json(self):
        """outputs data in json format"""
        json = {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'category': self.category
        }
        return json

    def __str__(self):
        return self.name
