from datetime import date
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .models import *
from .forms import FormLibro
from datetime import datetime





def inicio(request):
    return render(request, 'inicio.html') 


def vendedores(request):
    return render(request, 'vendedores.html')

def libros(request):
    return render(request, 'libros.html')


def crear_libro(request):
        
    if request.method == 'POST':
        form = FormLibro(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            fecha = data.get('fecha_publicacion')
            if not fecha:
                fecha = datetime.now() 
            
            libro = libro(
                titulo=data.get('titulo'),
                editorial=data.get('edad'),
                fecha_publicacion= fecha 
            )
            libro.save()

            listado_libros = libro.objects.all()
        
            return render(request,'listado_libros.html', {'listado_libros': listado_libros})
        
        else:
            return render(request, 'crear_libro.html', {'form': form})
            
    
    form_libro = FormLibro()
    
    return render(request, 'crear_libro.html', {'form': form_libro})

def listado_libros(request):
    
        nombre_de_busqueda = request.GET.get('nombre')
        if nombre_de_busqueda:
                
            listado_libros = libro.objects.filter(titulo__icointains=nombre_de_busqueda) 
        else:
            listado_libros = libro.objects.all()
            
        form = BusquedaLibro()
        
        return render(request, 'listado_libros.html', {'listado_libros': listado_libros, 'form': form})
        
        


 