from django.db import models

# Create your models here.
class Ticker(models.Model):
    Ticker_name = models.CharField(max_length = 100)
    Price = models.DecimalField(blank = False,decimal_places=5,max_digits=10)
    Market_cap = models.DecimalField(blank = False,decimal_places=5,max_digits=10)
