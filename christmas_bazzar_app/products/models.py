from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=80, blank=False)
    price = models.FloatField(blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to='products')
    is_available = models.BooleanField(default=True)
