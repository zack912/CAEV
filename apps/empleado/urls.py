from django.conf.urls import patterns, include, url


urlpatterns = patterns('apps.empleado.views',
	url(r'^empleado/$', 'view_lista_empleado_index', name="vista_lista_empleado_index"),
	url(r'^empleado/add$', 'view_lista_empleado_add', name="vista_lista_empleado_add"),
	url(r'^empleado/edit/(?P<id>.*)/$', 'view_lista_empleado_edit', name="vista_lista_empleado_edit"),
	url(r'^empleado/del/(?P<id>.*)/$', 'view_lista_empleado_del', name="vista_lista_empleado_del"),

	)