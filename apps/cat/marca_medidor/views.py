from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import marca_medidor
from .forms import marca_medidorForm
from django.http import HttpResponse,HttpResponseRedirect

def view_marca_medidor_index(request):
	lista_marca_medidor = marca_medidor.objects.all() 
	ctx = {'lista_marca_medidor':lista_marca_medidor}
	return render_to_response("marca_medidor/index.html",ctx,
		context_instance=RequestContext(request))


def view_marca_medidor_add(request):
	if request.method == "POST":
		formulario = marca_medidorForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/marca_medidor/")

		else:	
			formulario = marca_medidorForm(request.POST)
			ctx ={'form':formulario}
			return render_to_response("marca_medidor/agregar.html",ctx, 
				context_instance=RequestContext(request))
		
	else:
		formulario = marca_medidorForm()
		ctx = {'form':formulario}
		return render_to_response("marca_medidor/agregar.html",ctx,
			context_instance = RequestContext(request))


def view_marca_medidor_edit(request, id):
	marcmed = marca_medidor.objects.get(pk = id)
	if request.method == "POST":
		formulario = marca_medidorForm(request.POST, instance = marcmed)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/marca_medidor/")

		else:	
			formulario = marca_medidorForm(request.POST)
			ctx ={'form':formulario}
			return render_to_response("marca_medidor/actualizar.html",ctx, 
				context_instance=RequestContext(request))
		
	else:
		formulario = marca_medidorForm(instance = marcmed)
		ctx = {'form':formulario}
		return render_to_response("marca_medidor/actualizar.html",ctx,
			context_instance = RequestContext(request))


def view_marca_medidor_del(request, id):
	marcmed = marca_medidor.objects.get(pk = id)
	marcmed.status = False   # desactivando registros sin ser eliminados
	marcmed.save()
	return HttpResponseRedirect("/marca_medidor/")


		

	



