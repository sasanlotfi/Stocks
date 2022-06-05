from django.db import models
from django.urls import reverse
# Create your models here.
class Ticker(models.Model):
    Ticker_name = models.CharField(max_length = 100)
    Price = models.DecimalField(blank = False,decimal_places=5,max_digits=10)
    Market_cap = models.DecimalField(blank = False,decimal_places=5,max_digits=10)

    def __str__(self):
        return self.Ticker_name

    def get_absolute_url(self):
        return reverse("ticker_detail", args = (str(self.id),))
