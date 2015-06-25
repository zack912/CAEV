from django.conf.urls import patterns, include, url


urlpatterns = patterns('apps.cat.concepto_pago.views',
	url(r'^concepto_pago/$', 'view_concepto_pago_index', name="vista_concepto_pago_index"),
	url(r'^concepto_pago/add/$', 'view_concepto_pago_add', name="vista_concepto_pago_add"),
	url(r'^concepto_pago/edit/(?P<id>.*)/$', 'view_concepto_pago_edit', name="vista_concepto_pago_edit"),
	url(r'^concepto_pago/del/(?P<id>.*)/$', 'view_concepto_pago_del', name="vista_concepto_pago_del"),
	)