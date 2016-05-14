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

def proveedoresDetail(request, nit, template='proveedoresDetalle.html'):
    Proveedores = get_object_or_404(proveedores, pk=nit)
    return render_to_response(template, {'Proveedores': Proveedores}, context_instance=RequestContext(request))

def proveedoresDelete(request, id_nit):
    instance = get_object_or_404(proveedores, id=id_nit)
    instance.delete()
    messages.add_message(request, messages.SUCCESS, "El proveedor con nit: %s fue Eliminado!" % id)
    return HttpResponseRedirect("/proveedores/list/")

def proveedoresUpdate(request, id_nit):
    instance = get_object_or_404(proveedores, id=id_nit)
    form = proveedoresForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "El proveedor fue actualizado!")
            return HttpResponseRedirect("/proveedores/list/")

    return render(request, 'form_proveedores.html', {'form': form})
