from django.db import models

# Create your models here.
class Product(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=50)
    inventory = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
