from django.urls import path

from blog.views import inicio, vendedores, libros, crear_libro, listado_libros

urlpatterns = [
    path('', inicio, name='inicio'),
    path('vendedores/', vendedores, name='vendedores'),
    path('libros/', libros, name='libros'),
    path('crear-libro', crear_libro, name= 'crear_libro'),
    path('listado-libros', listado_libros, name= 'listado_libros')
   
]