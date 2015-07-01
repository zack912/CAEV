
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import tipo_movimiento
from .forms import tipo_movimientoForm
from django.http import HttpResponse,HttpResponseRedirect

def view_tipo_movimiento_index(request):
	lista_tipo_movimiento = tipo_movimiento.objects.all()
	ctx = {'lista_tipo_movimiento':lista_tipo_movimiento}
	return render_to_response("tipo_movimiento/index.html",ctx,
		context_instance=RequestContext(request))


def view_tipo_movimiento_add(request):
	if request.method == "POST":
		formulario = tipo_movimientoForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/tipo_movimiento/")
		else:
			formulario = tipo_movimientoForm(request.POST)
			ctx ={'form':formulario}
			return render_to_response("tipo_movimiento/agregar.html",ctx, 
				context_instance=RequestContext(request))
	
	else :
		formulario = tipo_movimientoForm()
		ctx ={'form':formulario}
		return render_to_response("tipo_movimiento/agregar.html",ctx, 
			context_instance=RequestContext(request))


def view_tipo_movimiento_edit(request,id):
	tm=tipo_movimiento.objects.get(pk=id)
	if request.method == "POST":
		formulario = tipo_movimientoForm(request.POST, instance=tm)
		if formulario.is_valid():
			formulario.save()
			return HttpResponse("/tipo_movimiento/")
		
		else:
			formulario = tipo_movimientoForm(request.POST)
			ctx ={'form':formulario}
			return render_to_response("tipo_movimiento/actualizar.html",ctx, 
				context_instance=RequestContext(request))
	
	else :
		formulario = tipo_movimientoForm(instance=tm)
		ctx ={'form':formulario}
		return render_to_response("tipo_movimiento/actualizar.html",ctx, 
			context_instance=RequestContext(request))



def view_tipo_movimiento_del(request,id):
	td = tipo_movimiento.objects.get(pk=id)
	td.delete()
	return HttpResponseRedirect("/tipo_movimiento/")
