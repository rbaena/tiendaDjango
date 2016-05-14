#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import proveedores

class proveedoresForm(forms.ModelForm):
	nit = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Entre nit proveedor'}))
	razonS = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Entre razón social'}))
	dirp = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Entre dirección del proveedor'}))
	tel = forms.CharField(widget=forms.TextInput(attrs={'class': 'error','placeholder': 'Entre teléfono del proveedor'}))
	class Meta:
		model = proveedores
		fields = ['nit','razonS','dirp','tel']
