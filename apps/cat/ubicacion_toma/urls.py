from django.conf.urls import patterns, include, url


urlpatterns = patterns('apps.cat.ubicacion_toma.views',
	url(r'^ubicacion_toma/$', 'view_ubicacion_toma_index', name="vista_ubicacion_toma_index"),
	url(r'^ubicacion_toma/add$', 'view_ubicacion_toma_add', name="vista_ubicacion_toma_add"),
	url(r'^ubicacion_toma/edit/(?P<id>.*)/$', 'view_ubicacion_toma_edit', name="vista_ubicacion_toma_edit"),
	url(r'^ubicacion_toma/del/(?P<id>.*)/$', 'view_ubicacion_toma_del', name="vista_ubicacion_toma_del"),	

	)