from __future__ import unicode_literals
from django.db import models
from proveedores.models import proveedores

# Create your models here.
class productos(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nit = models.ForeignKey(proveedores, null=True)
    nomprod = models.CharField(max_length=80)
    precioU = models.DecimalField(max_digits=5, decimal_places=2)
    descrip = models.TextField(blank=True)

    def __str__(self):
 		return self.idProducto
