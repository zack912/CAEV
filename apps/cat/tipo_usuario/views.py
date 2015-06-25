from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import tipo_usuario
from .forms import tipo_usuarioForm
from django.http import HttpResponse,HttpResponseRedirect

def view_tipo_usuario_index(request):
	lista_tipo_usuario = tipo_usuario.objects.all()
	ctx = {'lista_tipo_usuario':lista_tipo_usuario}
	return render_to_response("tipo_usuario/index.html",ctx,
		context_instance=RequestContext(request))


def view_tipo_usuario_add(request):
	if request.method == "POST":
		formulario = tipo_usuarioForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/tipo_usuario/")

		else:
			formulario = tipo_usuarioForm(request.POST)
			ctx = {'form':formulario}
			return render_to_response("tipo_usuario/agregar.html",ctx,
				context_instance = RequestContext(request))

	else:
		formulario = tipo_usuarioForm()
		ctx = {'form':formulario}
		return render_to_response("tipo_usuario/agregar.html",ctx,
			context_instance = RequestContext(request))


def view_tipo_usuario_edit(request,id):
	dt = tipo_usuario.objects.get(pk=id)
	if request.method == "POST":
		formulario = tipo_usuarioForm(request.POST, instance = dt)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/tipo_usuario/")

		else:
			formulario = tipo_usuarioForm(request.POST)
			ctx = {'form':formulario}
			return render_to_response("tipo_usuario/actualizar.html",ctx,
				context_instance = RequestContext(request))

	else:
		formulario = tipo_usuarioForm(instance = dt)
		ctx = {'form':formulario}
		return render_to_response("tipo_usuario/actualizar.html",ctx,
			context_instance = RequestContext(request))



def view_tipo_usuario_del(request,id):
	td = tipo_usuario.objects.get(pk=id)
	td.delete()
	return HttpResponseRedirect("/tipo_usuario/")