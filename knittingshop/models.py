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
            ('In stock', 'In stock'),
            ('To order', 'To order'),
        ],
        default='In stock'
    )
    item_materials = models.CharField(max_length=120, default="")
    item_colors = models.CharField(max_length=120, default="")
    item_has_spec_price = models.BooleanField(default=False)
    item_spec_price = models.PositiveIntegerField(default=15)  # TODO django-money
    item_spec_cond = models.CharField(max_length=120, default="", blank=True)

    def __str__(self):
        return self.item_name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    country = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    street = models.CharField(max_length=100, default='')
    home = models.PositiveIntegerField(default=0)
    apartment = models.PositiveIntegerField(default=0)
    phone = models.CharField(max_length=12, default='')  # TODO django-phonenumber-field
    zip = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.get_full_name()


class Purchase(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    chosen_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField('purchase date', default=timezone.now)

    def __str__(self):
        return '{}  buys {}'.format(self.user.__str__(), self.chosen_item.__str__())


class Question(models.Model):
    name = models.CharField(max_length=120, default="")
    email = models.EmailField()
    question = models.TextField()

    def __str__(self):
        return str(self.question)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
