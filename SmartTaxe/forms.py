from django import forms
from django.forms import ModelForm
from .models import Tax


# Create a tax calculation form

class TaxForm(ModelForm):
    class Meta:
        model = Tax
        fields = ('income', 'loan')
