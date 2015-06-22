from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Pagos
from .forms import PagosForm
from django.http import HttpResponse, HttpResponseRedirect

def view_get_contrato(request):
	return render_to_response("pagos/get.html",
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
		ctx = {'form':formulario}
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
