from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from orders.models import Order


class Product(models.Model):
    name = models.CharField(max_length=80, blank=False)
    price = models.FloatField(blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to='products')
    is_available = models.BooleanField(default=True)
    is_shipped = models.BooleanField(default=False)
    sold_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sold_by')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='sold_to', blank=True, null=True)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'product',)

