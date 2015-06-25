from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.cat.consumo_promedio.views',
	url(r'^consumo_promedio/$', 'view_consumo_promedio_index', name="vista_consumo_promedio_index"),
	url(r'^consumo_promedio/add/$', 'view_consumo_promedio_add', name="vista_consumo_promedio_add"),
	url(r'^consumo_promedio/edit/(?P<id>.*)/$', 'view_consumo_promedio_edit', name="vista_consumo_promedio_edit"),
	url(r'^consumo_promedio/del/(?P<id>.*)/$', 'view_consumo_promedio_del', name="vista_consumo_promedio_del"),
	)