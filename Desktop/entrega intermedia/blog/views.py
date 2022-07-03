from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import cliente

# Create your views here.

# def inicio(request):
#     return HttpResponse('vista inicio')

# def clientes(request):
#     return HttpResponse('vista clientes')

# def vendedores(request):
#     return HttpResponse('vista vendedores')

# def libros(request):
#     return HttpResponse('vista libros')


def inicio(request):
    return render(request, "templates/inicio.html")

def clientes(request):
    return render(request, "templates/clientes.html")

def vendedores(request):
    return render(request, "templates/vendedores.html")

def libros(request):
    return render(request, "templates/libros.html")