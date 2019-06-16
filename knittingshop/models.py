import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_description = models.TextField()
    item_main_photo_path = models.CharField(max_length=120, default="")

    # item_main_photo = models.ImageField(upload_to='img/main/', max_length=255, null=True, blank=True)
    # tem_pictures_list = []
    # TODO pip install Pillow for image field

    item_main_photo = models.ImageField(upload_to='item_image', blank=True)

    def __str__(self):
        return self.item_name


# class UserProfile(models.Model):
#     user = models.OneToOneField(User)
#
#     def create_user(self):
#         pass

# class Basket(models.Model):
#     user = models.OneToOneField(UserProfile)


