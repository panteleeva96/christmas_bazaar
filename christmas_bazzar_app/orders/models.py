from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=False)
    family_name = models.CharField(max_length=50, blank=False)
    telephone_number = models.CharField(max_length=10, blank=False)
    delivery_address = models.CharField(max_length=150, blank=False)
    order_date = models.DateTimeField(blank=False)
    amount = models.FloatField(blank=False)
