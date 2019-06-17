import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.db.models.signals import post_save


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


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    phone = models.PositiveIntegerField(default=0)  # TODO mask

    def __str__(self):
        return self.user.get_full_name()

    # basket = models.OneToOneField(Basket)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
# class Basket(models.Model):
#     user = models.OneToOneField(UserProfile)
