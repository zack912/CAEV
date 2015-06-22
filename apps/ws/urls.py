from django.conf.urls import patterns, include, url


urlpatterns = patterns('apps.ws.views',
	url(r'^ws/cliente/contrato/(?P<contrato>.*)/$', 'view_cliente_contrato_ajax', name="vista_cliente_contrato_ajax"),
	url(r'^ws/tipo_servicio/(?P<id>.*)/$', 'view_tipo_servicio_ajax', name="view_tipo_servicio_ajax"),
	url(r'^ws/tipo_usuario/(?P<id>.*)/$', 'view_tipo_usuario_ajax', name="view_tipo_usuario_ajax"),
	
	)