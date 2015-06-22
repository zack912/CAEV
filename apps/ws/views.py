from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core import serializers
from django.http import HttpResponse
import json
from apps.cliente.models import Cliente
from django.core.exceptions import ObjectDoesNotExist
from apps.cat.tipo_servicio.models import tipo_servicio
from apps.cat.tipo_usuario.models import tipo_usuario

def view_cliente_contrato_ajax(request,contrato):
	if request.method == "GET":
		data = serializers.serialize("json",Cliente.objects.filter(status=True,Contrato=contrato))
		return HttpResponse(data,content_type='application/json')
	else:
		return HttpResponse("No hay ningun problema")

def view_tipo_servicio_ajax(request,id):

	if request.method == "GET":
		try:
			ts = tipo_servicio.objects.filter(pk=id)
			data = serializers.serialize("json",ts)
			return HttpResponse(data,content_type='application/json')
		except ObjectDoesNotExist:
			status = {}
			data = serializers.serialize("json",status)
			return HttpResponse(data,content_type='application/json')
	else:
		return HttpResponse("No hay ningun problema")


def view_tipo_usuario_ajax(request,id):

	if request.method == "GET":
		try:
			ts = tipo_usuario.objects.filter(pk=id)
			data = serializers.serialize("json",ts)
			return HttpResponse(data,content_type='application/json')
		except ObjectDoesNotExist:
			status = {}
			data = serializers.serialize("json",status)
			return HttpResponse(data,content_type='application/json')
	else:
		return HttpResponse("No hay ningun problema")
