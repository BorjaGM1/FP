from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, "selfservice/home.html")


def about(request):
    return render(request, "selfservice/about.html")


def carta(request):
    return render(request, "selfservice/carta.html")


def ofertas(request):
    return render(request, "selfservice/ofertas.html")


def vegetal(request):
    return render(request, "selfservice/vegetal.html")


def carrito(request):
    return render(request, "selfservice/carrito.html")
