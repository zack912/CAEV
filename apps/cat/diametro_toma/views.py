from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import diametro_toma
from .forms import diametro_tomaForm
from django.http import HttpResponse,HttpResponseRedirect

def view_diametro_toma_index(request):
	lista_diametro_toma = diametro_toma.objects.all()
	ctx = {'lista_diametro_toma':lista_diametro_toma}
	return render_to_response("diametro_toma/index.html",ctx,
		context_instance=RequestContext(request))


def view_diametro_toma_add(request):
	if request.method == "POST":
		formulario = diametro_tomaForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/diametro_toma/")
		
		else:
			formulario = diametro_tomaForm(request.POST)
			ctx ={'form':formulario}
			return render_to_response("diametro_toma/agregar.html",ctx, 
				context_instance=RequestContext(request))
	
	else :
		formulario = diametro_tomaForm()
		ctx ={'form':formulario}
		return render_to_response("diametro_toma/agregar.html",ctx, 
			context_instance=RequestContext(request))


def view_diametro_toma_edit(request,id):
	dt=diametro_toma.objects.get(pk=id)
	if request.method == "POST":
		formulario = diametro_tomaForm(request.POST, instance=dt)
		if formulario.is_valid():
			formulario.save()
			return HttpResponse("/diametro_toma/")
		
		else:
			formulario = diametro_tomaForm(request.POST)
			ctx ={'form':formulario}
			return render_to_response("diametro_toma/actualizar.html",ctx, 
				context_instance=RequestContext(request))
	
	else :
		formulario = diametro_tomaForm(instance=dt)
		ctx ={'form':formulario}
		return render_to_response("diametro_toma/actualizar.html",ctx, 
			context_instance=RequestContext(request))



def view_diametro_toma_del(request,id):
	td = diametro_toma.objects.get(pk=id)
	td.delete()
	return HttpResponseRedirect("/diametro_toma/")

