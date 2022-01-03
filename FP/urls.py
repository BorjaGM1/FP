"""FP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from selfservice import views as selfservice_views
from kitchen import views as kitchen_views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', selfservice_views.index, name="index"),
    path('home/', selfservice_views.home, name="home"),
    path('about/', selfservice_views.about, name="about"),
    path('carta/', selfservice_views.carta, name="carta"),
    path('ofertas/', selfservice_views.ofertas, name="ofertas"),
    path('vegetal/', selfservice_views.vegetal, name="vegetal"),
    path('carrito/', selfservice_views.carrito, name="carrito"),
    path('login/', kitchen_views.login, name="login"),
    path('listado/', kitchen_views.listado, name="listado"),
    path('producto/<int:pk>/', selfservice_views.ProductView.as_view(), name='producto'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
