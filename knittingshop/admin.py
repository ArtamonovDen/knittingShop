from django.contrib import admin

from .models import Item
from .models import UserProfile

# Register your models here.

admin.site.register(Item)
admin.site.register(UserProfile)
