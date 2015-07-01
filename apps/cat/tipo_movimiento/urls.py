from django.conf.urls import patterns, include, url


urlpatterns = patterns('apps.cat.tipo_movimiento.views',
	url(r'^tipo_movimiento/$', 'view_tipo_movimiento_index', name="vista_tipo_movimiento_index"),
	url(r'^tipo_movimiento/add/$', 'view_tipo_movimiento_add', name="vista_tipo_movimiento_add"),
	url(r'^tipo_movimiento/edit/(?P<id>.*)/$', 'view_tipo_movimiento_edit', name="vista_tipo_movimiento_edit"),
	url(r'^tipo_movimiento/del/(?P<id>.*)/$', 'view_tipo_movimiento_del', name="vista_tipo_movimiento_del"),
	)