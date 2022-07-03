from django.urls import path
from .views import clientes, vendedores, libros, inicio

urlpatterns = [
    path('', inicio),
    path('clientes/', clientes),
    path('vendedores/', vendedores),
    path('libros/', libros),
]