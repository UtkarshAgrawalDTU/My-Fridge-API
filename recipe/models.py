from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Recipe(models.Model):
    
    name = models.CharField(max_length=200, default="Not provided", blank=True)
    img_url = models.URLField(blank= True)
    author = models.CharField(max_length=200, default="Unknown", blank=True)
    prepare_time = models.CharField(max_length=100, default="Unknown", blank= True)
    cook_time = models.CharField(max_length=100, default="Unknown", blank= True)
    total_time = models.CharField(max_length=100, default="Unknown", blank= True)
    directions = models.TextField(default = "Unknown", blank= True)
    ingredients_list = models.TextField(blank= True)
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes')

    def __str__(self):
        return f'{self.name} - {self.author}'


    
