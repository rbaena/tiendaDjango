from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from .models import proveedores
from productos.models import productos
from .forms import proveedoresForm

def inicio(request):
    Proveedores = proveedores.objects.all()
    Productos = productos.objects.all()
    return render(request, 'inicio.html', {'Proveedores': Proveedores, 'Productos': Productos})

def proveedoresCreation(request, template='proveedoresForm.html'):
    form = proveedoresForm()
    if request.method == "POST":
        form = proveedoresForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'proveedoresNuevo.html')
    kwvars = {
        "form": form,
    }
    return render_to_response(template, kwvars, context_instance=RequestContext(request))

def proveedoresList(request):
    Proveedores = proveedores.objects.all()
    return render(request, 'proveedoresListado.html', {'Proveedores': Proveedores})

def proveedoresDetail(request, id, template='proveedoresDetalle.html'):
    Proveedores = get_object_or_404(proveedores, pk=id)
    return render_to_response(template, {'Proveedores': Proveedores}, context_instance=RequestContext(request))

def proveedoresDelete(request, id_nit):
    instance = get_object_or_404(proveedores, id=id_nit)
    instance.delete()
    Proveedores = proveedores.objects.all()
    return render(request, 'proveedoresListado.html', {'Proveedores': Proveedores})

def proveedoresUpdate(request, id_nit):
    instance = get_object_or_404(proveedores, id=id_nit)
    form = proveedoresForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            Proveedores = proveedores.objects.all()
            return render(request, 'proveedoresListado.html', {'Proveedores': Proveedores})
    return render(request, 'proveedoresDetalle.html', {'form': form})
