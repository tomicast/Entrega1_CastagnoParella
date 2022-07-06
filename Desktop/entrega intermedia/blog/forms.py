from django import forms

class FormLibro(forms.Form):
    titulo = forms.CharField(max_length=30)
    editorial = forms.CharField(max_length=30)
    fecha_publicacion = forms.DateField(required=False)
    
class BusquedaLibro(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)