from django.shortcuts import render, HttpResponse


def login(request):
    return render(request, "kitchen/login.html")


def listado(request):
    return render(request, "kitchen/listado.html")