from django.contrib.auth.models import User
from django.db import models


class Stock_ID(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_ticker = models.CharField(max_length=5)
    company_name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.stock_ticker}, {self.company_name}'


class Saved_Predictions(models.Model):
    stock_ticker = models.CharField(max_length=5)
    date_predicted = models.CharField(max_length=10)
    img = models.TextField()

    def __str__(self):
        return f'{self.stock_ticker}, {self.date_predicted}'

