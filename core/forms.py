from django import forms 
from django.forms import ModelForm
from .models import Proveedor

class ProveedorForm(ModelForm):
    class Meta:
        model= Proveedor
        fields =['Idprov', 'nombre','telefono','direccion','email','pais','moneda']