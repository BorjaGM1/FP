from django.db import models
from django.conf import settings


class Item(models.Model):

    title = models.CharField(max_length=100)
    price = models.FloatField()
    imglink = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=400)

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    title = models.CharField(max_length=100)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):
    ordered_date = models.DateTimeField(auto_now_add=True)
    articles = models.ManyToManyField(Item)

    def __str__(self):
        return self.id
