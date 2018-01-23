from django.db import models
#Basic models for the store currentlyonly has id for primary key purposes and name

class Category(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 30, unique = True)

    def __str__(self):
        return self.name


class Game(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50, unique = True)
    category = models.ForeignKey(Category, null = False, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

# Create your models here.
