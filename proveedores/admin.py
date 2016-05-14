from django.contrib import admin

# Register your models here.
from .models import proveedores

class proveedoresAdmin(admin.ModelAdmin):
    fields = ['nit','razonS','dirp','tel']

admin.site.register(proveedores)
