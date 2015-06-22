from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Cliente
from .forms import ClienteForm
from django.http import HttpResponse,HttpResponseRedirect

def view_busqueda_contrato(request,contrato,digito):
	lista_cliente = Cliente.objects.filter(status=True,Contrato=contrato,Dig_verf=digito) #para filtrar clientes activos
	print lista_cliente, 'lista'
	ctx = {'lista_cliente':lista_cliente}
	return render_to_response("pagos/index.html",ctx,
		context_instance = RequestContext(request))


def view_lista_cliente_buscar(request,tipo,consulta):
	if str(tipo) == "zona":
		lista_cliente = Cliente.objects.filter(status=True,Zona=str(consulta)) #para filtrar clientes activos
		print "zona"
		print lista_cliente
	if str(tipo) == "nombre":
		#nombre = str(consulta)
		#minuscula = nombre.lower()
		lista_cliente = Cliente.objects.filter(status=True,Nombre__startswith=consulta) #para filtrar clientes activos
		print "es nombre"
	ctx = {'lista_cliente':lista_cliente}
	return render_to_response("cliente/activar.html",ctx,
		context_instance = RequestContext(request))


def view_lista_cliente_activos(request):
	lista_cliente = Cliente.objects.filter(status=True) #para filtrar clientes activos
	ctx = {'lista_cliente':lista_cliente}
	return render_to_response("cliente/activar.html",ctx,
		context_instance = RequestContext(request))

def view_lista_cliente_inactivos(request):
	lista_cliente = Cliente.objects.filter(status=False) #para filtrar clientes activos
	ctx = {'lista_cliente':lista_cliente}
	return render_to_response("cliente/desactivar.html",ctx,
		context_instance = RequestContext(request))



def view_lista_cliente_index(request):
	lista_cliente = Cliente.objects.filter(status=True) #para filtrar clientes activos
	ctx = {'lista_cliente':lista_cliente}
	return render_to_response("cliente/index.html",ctx,
		context_instance = RequestContext(request))


def view_lista_cliente_add(request):
	if request.method == "POST":
		print "POST add"
		formulario = ClienteForm(request.POST)
		if formulario.is_valid():
			c = formulario.save(commit=False)
			c.status= True
			c.save()
			return HttpResponseRedirect("/cliente/add/")
		else:
			formulario = ClienteForm(request.POST)

			ctx = {'form':formulario}
			return render_to_response("cliente/agregar.html",ctx,
				context_instance = RequestContext(request))

	else:
		print "GET add"
		formulario = ClienteForm()
		ctx = {'form':formulario}
		return render_to_response("cliente/agregar.html",ctx,
			context_instance = RequestContext(request))


def view_lista_cliente_edit(request,id):
	dt = Cliente.objects.get(pk=id)
	if request.method == "POST":
		formulario = ClienteForm(request.POST,instance = dt)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("/cliente/")

		else:
			formulario = ClienteForm(request.POST)
			ctx = {'form':formulario}
			return render_to_response("cliente/actualizar.html",ctx,
				context_instance = RequestContext(request))

	else:
		formulario = ClienteForm(instance = dt)
		ctx = {'form':formulario}
		return render_to_response("cliente/actualizar.html",ctx,
			context_instance = RequestContext(request))


def view_lista_cliente_activar(request,id):
	dt = Cliente.objects.get(pk=id)
	dt.status= True   # activando registros sin ser eliminados
	dt.save()
	return HttpResponseRedirect("/cliente/inactivos/")


def view_lista_cliente_del(request,id):
	dt = Cliente.objects.get(pk=id)
	dt.status= False   # desactivando registros sin ser eliminados
	dt.save()
	return HttpResponseRedirect("/cliente/activos")