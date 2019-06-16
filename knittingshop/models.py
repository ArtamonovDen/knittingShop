import datetime

from django.db import models
from django.utils import timezone


class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_description = models.TextField()
    item_main_photo_path = models.CharField(max_length=120, default="")
    #item_main_photo = models.ImageField(upload_to='img/main/', max_length=255, null=True, blank=True)
    #tem_pictures_list = []
    # TODO pip install Pillow for image field

    def __str__(self):
        return self.item_name

