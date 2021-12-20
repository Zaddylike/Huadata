from django.db import models
from django.db.models.base import Model

# Create your models here.

class Product(models.Model):
    pid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 20, null = False)
    price = models.IntegerField(null = False)
    url = models.URLField(max_length = 200, null = False)
    photo_url = models.URLField(max_length = 200, null = False)
    def __str__(self):
        return self.name