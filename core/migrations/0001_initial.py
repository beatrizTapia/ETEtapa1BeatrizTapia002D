# Generated by Django 3.2.5 on 2021-07-06 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('Idprov', models.IntegerField(primary_key=True, serialize=False, verbose_name='identificacion del proveedor')),
                ('nombre', models.CharField(max_length=60, verbose_name='Nombre del proveedor')),
                ('telefono', models.CharField(max_length=15, verbose_name='Telefono del proveedor')),
                ('direccion', models.CharField(max_length=60, verbose_name='Direccion del proveedor')),
                ('email', models.CharField(max_length=40, verbose_name='Email del proveedor')),
                ('pais', models.CharField(max_length=40, verbose_name='pais del proveedor')),
                ('moneda', models.CharField(max_length=10, verbose_name='moneda del proveedor')),
            ],
        ),
    ]
