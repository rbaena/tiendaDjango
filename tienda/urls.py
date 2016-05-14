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
)
