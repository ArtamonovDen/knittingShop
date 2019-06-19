from django.contrib import admin

from .models import Item, UserProfile, Purchase, Question

# Register your models here.

admin.site.register(Item)
admin.site.register(UserProfile)
admin.site.register(Purchase)
admin.site.register(Question)