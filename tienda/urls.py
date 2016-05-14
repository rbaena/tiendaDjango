from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'proveedores.views.inicio', name='inicio'),
    url(r'^proveedores/nuevo/$','proveedores.views.proveedoresCreation' , name='proveedores_nuevo'),
    url(r'^proveedores/listado/$','proveedores.views.proveedoresList' , name='proveedores_listado'),
    url(r'^proveedor/(?P<id_nit>\d+)$','proveedores.views.proveedoresUpdate', name='proveedor_detalle'),
    url(r'^proveedor_e/(?P<id_nit>\d+)$','proveedores.views.proveedoresDelete', name='proveedor_borrar'),
    url(r'^productos/nuevo/$','productos.views.productosCreation', name='productos_nuevo'),
    url(r'^productos/listado/$','productos.views.productosList', name='productos_listado'),
    url(r'^producto/(?P<id_Producto>\d+)$','productos.views.productosUpdate', name='productos_detalle'),
    url(r'^producto_e/(?P<id_Producto>\d+)$','productos.views.productosDelete', name='productos_borrar'),
)
