from __future__ import unicode_literals
from django.db import models

# Create your models here.
class proveedores(models.Model):
    nit = models.CharField(max_length=20)
    razonS = models.CharField(max_length=80)
    dirp = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)

    def __str__(self):
 		return self.nit
