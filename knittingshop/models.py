import datetime

from django.db import models
from django.utils import timezone


class Item(models.Model):
    item_name = models.CharField(max_length=200)

    # TODO

    def __str__(self):
        return self.question_text


class Basket(models.Model):
    basket_name = models.CharField(max_length=200)
    # customer = models.ForeignKey(User, on_delete=models.CASCADE)
    # TODO
