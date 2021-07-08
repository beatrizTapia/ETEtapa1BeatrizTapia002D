from django.urls import path
from .views import inicio, proveedor, form_proveedor, form_mod_proveedor, form_del_proveedor

urlpatterns = [
    path ('', inicio, name='inicio'),
    path('proveedor', proveedor, name='proveedor'),
    path('form-proveedor', form_proveedor, name="form_proveedor"),
    path('form-mod-proveedor/<id>', form_mod_proveedor, name="form_mod_proveedor"),
    path('form-del-proveedor/<id>', form_del_proveedor, name="form_del_proveedor"),
]