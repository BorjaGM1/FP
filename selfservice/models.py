import self as self
from django.db import models
from django.conf import settings


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    imglink = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=400)

    def __str__(self):
        return self.title


class Order(models.Model):
    ordered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    @property
    def get_item_objects(self):
        orderitems = self.orderitem_set.all()
        return orderitems


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.item.title

    @property
    def get_title(self):
        title = self.item.title
        return title

    @property
    def get_price(self):
        price = self.item.price
        return price

    @property
    def get_total(self):
        total = self.item.price * self.quantity
        return total
