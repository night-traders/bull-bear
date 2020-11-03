
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Stock(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, null=True)
    ticker = models.CharField(max_length=64, null=True)
    price_current = models.CharField(max_length=100, null=True)
    price_open = models.CharField(max_length=100, null=True)
    previous_close = models.CharField(max_length=64, null=True)
    price_high = models.CharField(max_length=64, null=True)
    price_low = models.CharField(max_length=64,null=True)


    def __str__(self):
        return self.name      