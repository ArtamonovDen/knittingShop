import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.db.models.signals import post_save


class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_description = models.TextField()
    item_main_photo_path = models.CharField(max_length=120, default="")
    pub_date = models.DateTimeField('date published', default=timezone.now)

    # item_main_photo = models.ImageField(upload_to='img/main/', max_length=255, null=True, blank=True)
    # tem_pictures_list = []
    # TODO pip install Pillow for image field

    item_main_photo = models.ImageField(upload_to='item_image', blank=True)

    def __str__(self):
        return self.item_name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    phone = models.PositiveIntegerField(default=0)  # TODO mask

    # basket  =models.OneToOneField(Basket, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name()

    # basket = models.OneToOneField(Basket)

    # создание и доступ к корзине
    # u = UserProfile.obects(pk=3)
    # u.basket_set.create()
    # Basket.objects.filter(user = u)


class Basket(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    chosen_items = models.ManyToManyField(Item)

    #i = Items.objects.get(pk = pk)
    #b.chosen_items.add(i)
    # .get() чтобы получить

    #Publication.objects.get(id=4).article_set.all()
    #Article.objects.filter(publications__id=1)
    def __str__(self):
        return '{}\'s basket '.format(self.user.__str__())


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
