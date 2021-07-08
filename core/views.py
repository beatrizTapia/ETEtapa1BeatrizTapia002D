from django.shortcuts import render, redirect
from .models import Proveedor
from .forms import ProveedorForm


def proveedor(request):

    proveedor = Proveedor.objects.all()

    datos = {
        'proveedor': proveedor
    }
    return render(request, 'core/proveedor.html', datos)

def inicio(request):

    return render(request, 'core/inicio.html')

def form_proveedor(request):

    datos = {
        'form':ProveedorForm()
    }
    if request.method =='POST':
        formulario=ProveedorForm(data=request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Datos guardados correctamente"
    return render(request, 'core/form_proveedor.html', datos)

def form_mod_proveedor(request,id):
    proveedor = Proveedor.objects.get(Idprov =id)

    datos = {
        'form':ProveedorForm(instance=proveedor)
    }
    if request.method =='POST':
        formulario=ProveedorForm(data=request.POST,instance=proveedor)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Datos modificados correctamente"    
    return render(request,'core/form_mod_proveedor.html', datos)

def form_del_proveedor(request, id):
    proveedor = Proveedor.objects.get(Idprov=id)

    proveedor.delete()

    return redirect(to="proveedor")

    
# Create your views here.
