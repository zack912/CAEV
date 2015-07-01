from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Pagos
from .forms import PagosForm, formCPago
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
import cStringIO as StringIO
import ho.pisa as pisa
import cgi


# p = Pagos.objects.filter(concepto_pago='mensual',Cliente_id=2)


def pdf_pagos_anuales_cliente(request,id):
	lista = Pagos.objects.filter(concepto_pago='anual',Cliente_id=id)
	msg="Lista de pagos realizados por el alumno"
	ctx = {'lista':lista,'msg':msg}
	html = render_to_string("pagos/historial/anual_pdf.html",ctx,
			context_instance=RequestContext(request))
	return generar_pdf(html)


def pdf_pagos_mensuales_cliente(request,id):
	lista = Pagos.objects.filter(concepto_pago='mensual',Cliente_id=id)
	msg="Lista de pagos realizados por el alumno"
	ctx = {'lista':lista,'msg':msg}
	html = render_to_string("pagos/historial/mensual_pdf.html",ctx,
			context_instance=RequestContext(request))
	return generar_pdf(html)



def generar_pdf(html):
	result = StringIO.StringIO()
	pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(),content_type='application/pdf')
	return HttpResponse('Error al generar el PDF: %s' % cgi.escape(html))


def pdf_pagos_anuales(request):
	lista = Pagos.objects.filter(concepto_pago='anual')
	msg="Lista de pagos realizados por el alumno"
	ctx = {'lista':lista,'msg':msg}
	html = render_to_string("pagos/historial/anual_pdf.html",ctx,
			context_instance=RequestContext(request))
	return generar_pdf(html)


def pdf_pagos_mensuales(request):
	lista = Pagos.objects.filter(concepto_pago='mensual')
	msg="Lista de pagos realizados por el alumno"
	ctx = {'lista':lista,'msg':msg}
	html = render_to_string("pagos/historial/mensual_pdf.html",ctx,
			context_instance=RequestContext(request))
	return generar_pdf(html)

def view_get_contrato(request):
	return render_to_response("pagos/get.html",
		context_instance = RequestContext(request))

def view_historial_pagos_anual(request):
	lista_pagos = Pagos.objects.filter(concepto_pago='anual')
	ctx = {'lista_pagos':lista_pagos}
	return render_to_response("pagos/historial/anual.html",ctx,
		context_instance = RequestContext(request))

def view_historial_pagos_mensual(request):
	lista_pagos = Pagos.objects.filter(concepto_pago='mensual')
	ctx = {'lista_pagos':lista_pagos}
	return render_to_response("pagos/historial/mensual.html",ctx,
		context_instance = RequestContext(request))


def view_lista_pagos_index(request):
	lista_pagos = Pagos.objects.all()
	ctx = {'lista_pagos':lista_pagos}
	return render_to_response("pagos/index.html",ctx,
		context_instance = RequestContext(request))

def view_lista_pagos_add(request):
	if request.method == "POST":
		formulario = PagosForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponse("/pagos/")

		else:
			formulario = PagosForm(request.POST)
			ctx = {'form':formulario}
			return render_to_response("pagos/agregar.html",ctx,
				context_instance = RequestContext(request))

	else:
		formulario = PagosForm()
		form_conc = formCPago()
		ctx = {'form':formulario,'form_conceptos':form_conc}
		return render_to_response("pagos/agregar.html",ctx,
			context_instance = RequestContext(request))

def view_lista_pagos_edit(request,id):
	dt = Pagos.objects.get(pk=id)
	if request.method == "POST":
		formulario = PagosForm(request.POST, instance= dt)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/pagos/")

		else:
			formulario = PagosForm(request.POST)
			ctx = {'form':formulario}
			return render_to_response("pagos/actualizar.html",ctx,
				context_instance = RequestContext(request))

	else:
		formulario = PagosForm(instance = dt)
		ctx = {'form':formulario}
		return render_to_response("pagos/actualizar.html",ctx,
			context_instance = RequestContext(request))


def view_lista_pagos_del(request,id):
	dt = Pagos.objects.get(pk=id)
	dt.delete()
	return HttpResponseRedirect("/pagos/")
