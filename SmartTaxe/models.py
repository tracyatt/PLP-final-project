from django.db import models


# Create your models here.
class Tax(models.Model):
    income = models.IntegerField(null=True)
    loan = models.IntegerField(null=True)
