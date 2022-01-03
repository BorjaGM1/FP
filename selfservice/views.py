from django.shortcuts import render
from .models import Item
from django.views import generic


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


def payment(request):
    form = ItemCreate
