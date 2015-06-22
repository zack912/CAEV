from django.conf.urls import patterns, include, url


urlpatterns = patterns('apps.pagos.views',
	url(r'^pagos/$', 'view_lista_pagos_index', name = "vista_lista_pagos_index"),
	url(r'^pagos/get/contrato/$', 'view_get_contrato', name = "vista_get_contrato"),
	url(r'^pagos/add$', 'view_lista_pagos_add', name="vista_pagos_add"),
	url(r'^pagos/edit/(?P<id>.*)/$', 'view_lista_pagos_edit', name="vista_lista_pagos_edit"),
	url(r'^pagos/del/(?P<id>.*)/$', 'view_lista_pagos_del', name="vista_lista_pagos_del"),
	)