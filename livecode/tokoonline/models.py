from django.db import models

# Create your models here.

class Barang(models.Model):
    image = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.CharField(max_length=255)