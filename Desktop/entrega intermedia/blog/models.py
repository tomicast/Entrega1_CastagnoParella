from string import octdigits
from django.db import models

# Create your models here.

class cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField(null=True)
    
    def __str__(self):
        return f'{self.nombre}'
    
class vendedor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField(null=True)
    
    def __str__(self):
        return f'{self.nombre}'

class libro(models.Model):
    titulo = models.CharField(max_length=30)
    editorial = models.CharField(max_length=30)
    fecha_publicacion = models.DateField(null=True)
    
    def __str__(self):
        return f'{self.titulo}'
