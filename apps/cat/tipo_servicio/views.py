from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import tipo_servicio
from .forms import tipo_servicioForm
from django.http import HttpResponse,HttpResponseRedirect

def view_tipo_servicio_index(request):
	lista_tipo_servicio = tipo_servicio.objects.all()
	ctx = {'lista_tipo_servicio':lista_tipo_servicio}
	return render_to_response("tipo_servicio/index.html",ctx,
		context_instance=RequestContext(request))


def view_tipo_servicio_add(request):
	if request.method =="POST":
		formulario = tipo_servicioForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/tipo_servicio/")

		else:
			formulario = tipo_servicioForm(request.POST)
			ctx = {'form':formulario}
			return render_to_response("tipo_servicio/agregar.html",ctx,
				context_instance = RequestContext(request))

	else:
		formulario = tipo_servicioForm()
		ctx = {'form':formulario}
		return render_to_response("tipo_servicio/agregar.html",ctx,
			context_instance = RequestContext(request))


def view_tipo_servicio_edit(request,id):
	ts = tipo_servicio.objects.get(pk=id)
	if request.method =="POST":
		formulario = tipo_servicioForm(request.POST, instance = ts)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/tipo_servicio/")

		else:
			formulario = tipo_servicioForm(request.POST)
			ctx = {'form':formulario}
			return render_to_response("tipo_servicio/actualizar.html",ctx,
				context_instance = RequestContext(request))

	else:
		formulario = tipo_servicioForm(instance = ts)
		ctx = {'form':formulario}
		return render_to_response("tipo_servicio/actualizar.html",ctx,
			context_instance = RequestContext(request))



def view_tipo_servicio_del(request,id):
	ts = tipo_servicio.objects.get(pk=id)
	ts.delete()
	return HttpResponseRedirect("/tipo_servicio/")

