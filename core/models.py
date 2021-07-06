from django.db import models

# Create your models here.
class Proveedor(models.Model):
    Idprov =models.IntegerField(primary_key=True, verbose_name='identificacion del proveedor')
    nombre =models.CharField(max_length=60, verbose_name='Nombre del proveedor')
    telefono = models.CharField(max_length=15, verbose_name='Telefono del proveedor')
    direccion = models.CharField(max_length=60, verbose_name='Direccion del proveedor')
    email = models.CharField(max_length=40, verbose_name='Email del proveedor')
    pais = models.CharField(max_length=40, verbose_name='pais del proveedor')
    moneda = models.CharField(max_length=10, verbose_name='moneda del proveedor')
   
    def __str__(self):
        return self.nombre
