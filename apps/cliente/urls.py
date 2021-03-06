from django.conf.urls import patterns, include, url


urlpatterns = patterns('apps.cliente.views',
	url(r'^cliente/$', 'view_lista_cliente_index', name="vista_lista_cliente_index"),
	url(r'^cliente/add/$', 'view_lista_cliente_add', name="vista_cliente_add"),
	url(r'^cliente/edit/(?P<id>.*)/$', 'view_lista_cliente_edit', name="vista_lista_cliente_edit"),
	url(r'^cliente/del/(?P<id>.*)/$', 'view_lista_cliente_del', name="vista_lista_cliente_del"),
	url(r'^cliente/activar/(?P<id>.*)/$', 'view_lista_cliente_activar', name="vista_lista_cliente_activar"),
	url(r'^cliente_contrato/(?P<contrato>.*)/digito/(?P<digito>.*)/$', 'view_busqueda_contrato', name="vista_buscar_contrato"),
	url(r'^cliente/(?P<tipo>.*)/(?P<consulta>.*)/$', 'view_lista_cliente_buscar', name="vista_lista_cliente_buscar"),
	url(r'^cliente/inactivos/$', 'view_lista_cliente_inactivos', name="vista_lista_cliente_inactivos"),
	url(r'^cliente/activos/$', 'view_lista_cliente_activos', name="vista_lista_cliente_activos"),
	url(r'^historial/anual/$', 'view_historial_anual',name="historial_anual"),
	url(r'^historial/mensual/$', 'view_historial_mensual',name="historial_mensual"),
	)
