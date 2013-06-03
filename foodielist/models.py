from django.db import models
from django.contrib.admin import ModelAdmin, site


class Foodie(models.Model):
    """
    Simple field for storing sign ups
    """
    name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    casual = models.BooleanField()
    fine = models.BooleanField()
    cooking = models.BooleanField()
    joined = models.DateTimeField(auto_now_add=True)


class FoodieAdmin(ModelAdmin):
    list_display = ("name", "id", "email", "casual", "fine", "cooking", "joined")

site.register(Foodie, FoodieAdmin)