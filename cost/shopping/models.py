from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Item(models.Model):
    user = models.ForeignKey(User)
    item = models.CharField(max_length = 100)
    store = models.CharField(max_length = 50)
    count = models.IntegerField(default = 0, max_length = 5)
    metric = models.CharField(default = "items", max_length = 10)

class UserItem(models.Model):
    buyer = models.ForeignKey(User)
    receiver = models.CharField(max_length = 30)
    item = models.CharField(max_length = 100)
    store = models.CharField(max_length = 50)
    count = models.IntegerField(default = 0, max_length = 5)
    metric = models.CharField(default = "items", max_length = 10)

class PickupLocation(models.Model):
    user = models.ForeignKey(User)
    address = models.CharField(max_length=300)

admin.site.register(Item)
admin.site.register(UserItem)
admin.site.register(PickupLocation)
