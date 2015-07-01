from django.conf.urls import patterns, include, url


urlpatterns = patterns('apps.cat.marca_medidor.views',
	url(r'^marca_medidor/$', 'view_marca_medidor_index', name="vista_marca_medidor_index"),
	url(r'^marca_medidor/add$', 'view_marca_medidor_add', name="vista_marca_medidor_add"),
	url(r'^marca_medidor/edit/(?P<id>.*)/$', 'view_marca_medidor_edit', name="vista_marca_medidor_edit"),
	url(r'^marca_medidor/del/(?P<id>.*)/$', 'view_marca_medidor_del', name = "vista_marca_medidor_del"),
	)
