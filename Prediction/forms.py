from django import forms
from .models import Ticker

class Ticker_Create(forms.ModelForm):
    class Meta:
        model = Ticker
        fields = ('Ticker_name','Price','Market_cap')

