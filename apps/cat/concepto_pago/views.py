from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import concepto_pago
from .forms import concepto_pagoForm
from django.http import HttpResponse,HttpResponseRedirect

def view_concepto_pago_index(request):
	lista_concepto_pago = concepto_pago.objects.all()
	ctx = {'lista_concepto_pago':lista_concepto_pago}
	return render_to_response("concepto_pago/index.html",ctx,
		context_instance=RequestContext(request))


def view_concepto_pago_add(request):
	if request.method == "POST":
		formulario = concepto_pagoForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/concepto_pago/")
		else:
			formulario = concepto_pagoForm(request.POST)
			ctx ={'form':formulario}
			return render_to_response("concepto_pago/agregar.html",ctx, 
				context_instance=RequestContext(request))
	
	else :
		formulario = concepto_pagoForm()
		ctx ={'form':formulario}
		return render_to_response("concepto_pago/agregar.html",ctx, 
			context_instance=RequestContext(request))


def view_concepto_pago_edit(request,id):
	cp=concepto_pago.objects.get(pk=id)
	if request.method == "POST":
		formulario = concepto_pagoForm(request.POST, instance=cp)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/concepto_pago/")
		
		else:
			formulario = concepto_pagoForm(request.POST)
			ctx ={'form':formulario}
			return render_to_response("concepto_pago/actualizar.html",ctx, 
				context_instance=RequestContext(request))
	
	else :
		formulario = concepto_pagoForm(instance=cp)
		ctx ={'form':formulario}
		return render_to_response("concepto_pago/actualizar.html",ctx, 
			context_instance=RequestContext(request))



def view_concepto_pago_del(request,id):
	td = concepto_pago.objects.get(pk=id)
	td.delete()
	return HttpResponseRedirect("/concepto_pago/")
