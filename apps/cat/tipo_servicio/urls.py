from django.conf.urls import patterns, include, url


urlpatterns = patterns('apps.cat.tipo_servicio.views',
	url(r'^tipo_servicio/$', 'view_tipo_servicio_index', name = "vista_tipo_servicio_index"),
	url(r'^tipo_servicio/add/$', 'view_tipo_servicio_add', name = "vista_tipo_servicio_add"),
	url(r'^tipo_servicio/edit/(?P<id>.*)/$', 'view_tipo_servicio_edit', name = "vista_tipo_servicio_edit"),
    url(r'^tipo_servicio/del/(?P<id>.*)/$', 'view_tipo_servicio_del', name = "vista_tipo_servicio_del"),
	)