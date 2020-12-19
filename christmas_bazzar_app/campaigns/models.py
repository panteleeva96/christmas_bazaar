from django.db import models


# Create your models here.
class Campaign(models.Model):
    name = models.CharField(max_length=70, blank=False)
    image = models.ImageField(upload_to='campaign')
    description = models.TextField()
    raised_money = models.FloatField(default=0)
