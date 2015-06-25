from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import consumo_promedio
from .forms import consumo_promedioForm
from django.http import HttpResponse,HttpResponseRedirect


def view_consumo_promedio_index(request):
	lista_consumo_promedio = consumo_promedio.objects.all()
	ctx = {'lista_consumo_promedio':lista_consumo_promedio}
	return render_to_response("consumo_promedio/index.html",ctx,
		context_instance=RequestContext(request))

def view_consumo_promedio_add(request):
	if request.method == "POST":
		formulario = consumo_promedioForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/consumo_promedio/")
		
		else:
			formulario = consumo_promedioForm(request.POST)
			ctx ={'form':formulario}
			return render_to_response("consumo_promedio/agregar.html",ctx, 
				context_instance=RequestContext(request))
	
	else :
		formulario = consumo_promedioForm()
		ctx ={'form':formulario}
		return render_to_response("consumo_promedio/agregar.html",ctx, 
			context_instance=RequestContext(request))



def view_consumo_promedio_edit(request,id):
	dt=consumo_promedio.objects.get(pk=id)
	if request.method == "POST":
		formulario = consumo_promedioForm(request.POST, instance=dt)
		if formulario.is_valid():
			formulario.save()
			return HttpResponse("/consumo_promedio/")
		
		else:
			formulario = consumo_promedioForm(request.POST)
			ctx ={'form':formulario}
			return render_to_response("consumo_promedio/actualizar.html",ctx, 
				context_instance=RequestContext(request))
	
	else :
		formulario = consumo_promedioForm(instance=dt)
		ctx ={'form':formulario}
		return render_to_response("consumo_promedio/actualizar.html",ctx, 
			context_instance=RequestContext(request))


def view_consumo_promedio_del(request,id):
	td = consumo_promedio.objects.get(pk=id)
	td.delete()
	return HttpResponseRedirect("/consumo_promedio/")