from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Empleado
from .forms import EmpleadoForm
from django.http import HttpResponse,HttpResponseRedirect

def view_lista_empleado_index(request):
	lista_empleado = Empleado.objects.all()
	ctx = {'lista_empleado':lista_empleado}
	return render_to_response("empleado/index.html",ctx,
		context_instance = RequestContext(request))

def view_lista_empleado_add(request):
	if request.method == "POST":
		formulario = EmpleadoForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/empleado/agregar")

		else:
			formulario = EmpleadoForm(request.POST)
			ctx = {'form':formulario}
			return render_to_response("empleado/agregar.html",ctx,
				context_instance = RequestContext(request))

	else:
		formulario = EmpleadoForm()
		ctx = {'form':formulario}
		return render_to_response("empleado/agregar.html",ctx,
			context_instance = RequestContext(request))



def view_lista_empleado_edit(request,id):
	dt = Empleado.objects.get(pk=id)
	if request.method == "POST":
		formulario = EmpleadoForm(request.POST, instance = dt)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/empleado/")

		else:
			formulario = EmpleadoForm(request.POST)
			ctx = {'form':formulario}
			return render_to_response("empleado/actualizar.html",ctx,
				context_instance = RequestContext(request))

	else:
		formulario = EmpleadoForm(instance = dt)
		ctx = {'form':formulario}
		return render_to_response("empleado/actualizar.html",ctx,
			context_instance = RequestContext(request))



def view_lista_empleado_del(request,id):
	ts = Empleado.objects.get(pk=id)
	ts.delete()
	return HttpResponseRedirect("/empleado/")
