from django.contrib import admin

# Register your models here.
from .models import productos

class productosAdmin(admin.ModelAdmin):
    fields = ['nomprod','precioU','descrip']

admin.site.register(productos)
