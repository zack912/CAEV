from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import ubicacion_toma
from .forms import ubicacion_tomaForm
from django.http import HttpResponse,HttpResponseRedirect

def view_ubicacion_toma_index(request):
	lista_ubicacion_toma = ubicacion_toma.objects.all()
	ctx = {'lista_ubicacion_toma':lista_ubicacion_toma}
	return render_to_response("ubicacion_toma/index.html",ctx,
		context_instance=RequestContext(request))


def view_ubicacion_toma_add(request):
	if request.method == "POST":
		formulario = ubicacion_tomaForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/ubicacion_toma/")

		else:
			formulario = ubicacion_tomaForm(request.POST)
			ctx = {'form':formulario}
			return render_to_response("ubicacion_toma/agregar.html",ctx,
				context_instance = RequestContext(request))

	else:
		formulario = ubicacion_tomaForm()
		ctx ={'form':formulario}
		return render_to_response("ubicacion_toma/agregar.html",ctx,
			context_instance = RequestContext(request))



def view_ubicacion_toma_edit(request,id):
	dt = ubicacion_toma.objects.get(pk=id)
	if request.method == "POST":
		formulario = ubicacion_tomaForm(request.POST, instance = dt)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/ubicacion_toma/")

		else:
			formulario = ubicacion_tomaForm(request.POST)
			ctx = {'form':formulario}
			return render_to_response("ubicacion_toma/actualizar.html",ctx,
				context_instance = RequestContext(request))

	else:
		formulario = ubicacion_tomaForm(instance = dt)
		ctx ={'form':formulario}
		return render_to_response("ubicacion_toma/actualizar.html",ctx,
			context_instance = RequestContext(request))


def view_ubicacion_toma_del(request,id):
	td = ubicacion_toma.objects.get(pk=id)
	td.delete()
	return HttpResponseRedirect("/ubicacion_toma/")

