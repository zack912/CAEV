from django.conf.urls import patterns, include, url


urlpatterns = patterns('apps.cat.diametro_toma.views',
	url(r'^diametro_toma/$', 'view_diametro_toma_index', name="vista_diametro_toma_index"),
	url(r'^diametro_toma/add/$', 'view_diametro_toma_add', name="vista_diametro_toma_add"),
	url(r'^diametro_toma/edit/(?P<id>.*)/$', 'view_diametro_toma_edit', name="vista_diametro_toma_edit"),
	url(r'^diametro_toma/del/(?P<id>.*)/$', 'view_diametro_toma_del', name="vista_diametro_toma_del"),
	)