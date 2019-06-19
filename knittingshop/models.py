import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.db.models.signals import post_save

class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_description = models.TextField()
    item_main_photo = models.ImageField(upload_to='item_image', blank=True)
    item_pub_date = models.DateTimeField('date published', default=timezone.now)
    item_price = models.PositiveIntegerField(default=25)  # TODO django-money
    item_size = models.PositiveIntegerField(default=25)
    item_tools = models.CharField(max_length=120, default="")
    item_kit = models.CharField(max_length=120, default="")
    item_availability = models.CharField(
        max_length=30,
        choices=[
            ('Available', 'Available'),
            ('In order', 'In order'),
            ('Not available', 'Not available')
        ],
        default='Available'
    )
    item_materials = models.CharField(max_length=120, default="")
    item_colors = models.CharField(max_length=120, default="")
    item_has_spec_price = models.BooleanField(default=False)
    item_spec_price = models.PositiveIntegerField(default=15)  # TODO django-money
    item_spec_cond = models.CharField(max_length=120, default="", blank=True)

    # item_main_photo = models.ImageField(upload_to='img/main/', max_length=255, null=True, blank=True)
    # tem_pictures_list = []
    # TODO pip install Pillow for image field

    def __str__(self):
        return self.item_name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    country = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    street = models.CharField(max_length=100, default='')
    home = models.PositiveIntegerField(default=0)
    apartment = models.PositiveIntegerField(default=0)
    phone = models.PositiveIntegerField(default=0)  # TODO django-phonenumber-field
    zip = models.PositiveIntegerField(default=0)

    # basket  =models.OneToOneField(Basket, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name()

    # basket = models.OneToOneField(Basket)

    # создание и доступ к корзине
    # u = UserProfile.obects(pk=3)
    # u.basket_set.create()
    # Basket.objects.filter(user = u)


class Purchase(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    chosen_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField('purchase date', default=timezone.now)

    def __str__(self):
        return '{}  buys {}'.format(self.user.__str__(), self.chosen_item.__str__())

    # i = Items.objects.get(pk = pk)
    # b.chosen_items.add(i)
    # .get() чтобы получить

    # Publication.objects.get(id=4).article_set.all()
    # Article.objects.filter(publications__id=1)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
