from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
  url(r'^admin/', include(admin.site.urls)),
  url(r'^', include('apps.cat.diametro_toma.urls')),
  url(r'^', include('apps.cat.marca_medidor.urls')),
  url(r'^', include('apps.cat.tipo_servicio.urls')),
  url(r'^', include('apps.cat.tipo_usuario.urls')),
  url(r'^', include('apps.cat.ubicacion_toma.urls')),
  url(r'^', include('apps.cat.consumo_promedio.urls')),
  url(r'^', include('apps.cat.concepto_pago.urls')),
  url(r'^', include('apps.cat.tipo_movimiento.urls')),
  url(r'^', include('apps.empleado.urls')),
  url(r'^', include('apps.cliente.urls')),
  url(r'^', include('apps.home.urls')),
  url(r'^', include('apps.pagos.urls')),
  url(r'^', include('apps.ws.urls')),
  
)