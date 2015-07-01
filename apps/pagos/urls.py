from django.conf.urls import patterns, include, url


urlpatterns = patterns('apps.pagos.views',
	url(r'^pagos/$', 'view_lista_pagos_index', name = "vista_lista_pagos_index"),
	url(r'^pagos/get/contrato/$', 'view_get_contrato', name = "vista_get_contrato"),
	url(r'^pagos/add$', 'view_lista_pagos_add', name="vista_pagos_add"),
	url(r'^pagos/edit/(?P<id>.*)/$', 'view_lista_pagos_edit', name="vista_lista_pagos_edit"),
	url(r'^pagos/del/(?P<id>.*)/$', 'view_lista_pagos_del', name="vista_lista_pagos_del"),
	url(r'^pagos/mensual/$', 'view_historial_pagos_mensual', name = "vista_pagos_mensual"),
	url(r'^pagos/mensual/pdf/$', 'pdf_pagos_mensuales', name = "pdf_pagos_mensuales"),
	url(r'^pagos/cliente/(?P<id>.*)/mensual/pdf/$', 'pdf_pagos_mensuales_cliente', name = "pdf_pagos_mensuales_cliente"),
	url(r'^pagos/anual/$', 'view_historial_pagos_anual', name = "vista_pagos_anual"),
	url(r'^pagos/anual/pdf/$', 'pdf_pagos_anuales', name = "pdf_pagos_anuales"),
	url(r'^pagos/cliente/(?P<id>.*)/anual/pdf/$', 'pdf_pagos_anuales_cliente', name = "pdf_pagos_anuales_cliente"),
	
	)
