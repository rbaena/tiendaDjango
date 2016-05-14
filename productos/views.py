from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from .models import productos
from proveedores.models import proveedores
from .forms import productosForm

def inicio(request):
    Proveedores = proveedores.objects.all()
    Productos = productos.objects.all()
    return render(request, 'inicio.html', {'Proveedores': Proveedores, 'Productos': Productos})

def productosCreation(request, template='productosForm.html'):
    form = productosForm()
    if request.method == "POST":
        form = productosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'productosNuevo.html')
    kwvars = {
        "form": form,
    }
    return render_to_response(template, kwvars, context_instance=RequestContext(request))

def productosList(request):
    Productos = productos.objects.all()
    return render(request, 'productosListado.html', {'Productos': Productos})

def productosDetail(request, idProducto, template='productosDetalle.html'):
    Productos = get_object_or_404(productos, pk=idProducto)
    return render_to_response(template, {'Productos': Productos}, context_instance=RequestContext(request))

def productosDelete(request, id_Producto):
    instance = get_object_or_404(productos, idProducto=id_Producto)
    instance.delete()
    Productos = productos.objects.all()
    return render(request, 'productosListado.html', {'Productos': Productos})

def productosUpdate(request, id_Producto):
    instance = get_object_or_404(productos, idProducto=id_Producto)
    form = productosForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            Productos = productos.objects.all()
            return render(request, 'productosListado.html', {'Productos': Productos})
    return render(request, 'productosDetalle.html', {'form': form})
