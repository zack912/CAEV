from django.conf.urls import patterns, include, url


urlpatterns = patterns('apps.cat.tipo_usuario.views',
	url(r'^tipo_usuario/$', 'view_tipo_usuario_index', name = "vista_tipo_usuario_index"),
	url(r'^tipo_usuario/add/$', 'view_tipo_usuario_add', name = "vista_tipo_usuario_add"),
	url(r'^tipo_usuario/edit/(?P<id>.*)/$', 'view_tipo_usuario_edit', name = "vista_tipo_usuario_edit"),
	url(r'^tipo_usuario/del/(?P<id>.*)/$', 'view_tipo_usuario_del', name = "vista_tipo_usuario_del"),
	)