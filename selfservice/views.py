from django.db.models.fields import json
from django.core.serializers import json
import json
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator

from .models import Item
from .models import *
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
import re
from django.shortcuts import redirect
from django.urls import reverse_lazy


def index(request):
    return render(request, "selfservice/index.html")


def home(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "selfservice/home.html", context)


def about(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "selfservice/about.html", context)


def carta(request):
    foodlist = Item.objects.all()
    return render(request, "selfservice/carta.html",
                  {'foodlist': foodlist})


def ofertas(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "selfservice/ofertas.html", context)


def vegetal(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "selfservice/vegetal.html", context)


def carrito(request):
    foodlist = Item.objects.all()
    return render(request, "selfservice/carrito.html", {'foodlist': foodlist})


def allfood(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "", context)


class FoodListView(generic.ListView):
    model = Item
    context_object_name = 'item_list'


class ProductView(generic.DetailView):
    model = Item
    context_object_name = 'product'
    template_name = 'selfservice/producto.html'


@csrf_exempt
def updatedone(request, *args, **kwargs):
    pk = kwargs.get('pk')
    up = get_object_or_404(Order, pk=pk)
    up.status = 'D'
    up.save()
    return cocina(request)


@csrf_exempt
def createorder(request):
    cartitems = request.body
    cartitems = json.loads(cartitems)
    print(cartitems)
    # acartitems = json.load(data)
    neworder = Order.objects.create()
    neworder.save()
    for product, value in cartitems.items():
        newitem = OrderItem.objects.create(quantity=value, item_id=product, order_id=neworder.id)
        newitem.save()

    return render(request, redirect("selfservice/enjoy.html"))


def enjoy2(request):
    return render(request, "selfservice/enjoy2.html")


def cocina(request):
    return render(request, "selfservice/pedidos.html",
                  {'productos': OrderItem.objects.all(), 'order': Order.objects.all()})

