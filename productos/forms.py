#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import productos
from proveedores.models import proveedores

class productosForm(forms.ModelForm):

	nomprod = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Entre nombre producto'}))
    precioU = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Entre precio unitario producto'}))
    descrip = forms.CharField(widget=forms.TextArea(attrs={'class': 'error','placeholder': 'Entre descripción producto'}))
    nit_id = forms.ChoiceField(widget=forms.Select(attrs={'class': 'error'}), choices = proveedores)

    class Meta:
        model = productos
        fields = ['nomprod','precioU','descrip','nit_id']
