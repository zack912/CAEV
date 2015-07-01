from django.db import models
from apps.cat.tipo_usuario.models import tipo_usuario
from apps.cat.tipo_servicio.models import tipo_servicio
from apps.cat.diametro_toma.models import diametro_toma
from apps.cat.marca_medidor.models import marca_medidor
from apps.cat.ubicacion_toma.models import ubicacion_toma
from apps.cat.consumo_promedio.models import consumo_promedio
import datetime

class Cliente(models.Model):
	"""Datos del cliente"""
	Zona = models.CharField(max_length=10,null=False,blank=False)
	Dig_verf = models.CharField(max_length=3,null=False,blank=False)
	Contrato = models.CharField(max_length=20,null=False,blank=False,unique=True)
	Fecha_Registro=models.DateField(default=datetime.datetime.now)
	Nombre= models.CharField(max_length=200,null=False,blank=False)
	RFC = models.CharField(max_length=20,null=False,blank=False)
	Telefono=models.CharField(max_length=10,null=False,blank=False)
	Calle = models.CharField(max_length=50,null=False,blank=False)
	Municipio = models.CharField(max_length=50,null=False,blank=False)
	No_Interior = models.CharField(max_length=5,null=False,blank=False)
	Colonia = models.CharField(max_length=45,null=False,blank=False)
	tipo_usuario = models.ForeignKey(tipo_usuario,null=False,blank=False)
	tipo_servicio = models.ForeignKey(tipo_servicio,null=False,blank=False)
	diametro_toma = models.ForeignKey(diametro_toma,null=False,blank=False)
	No_Medidor = models.IntegerField(max_length=10,null=False,blank=False)
	consumo_promedio = models.ForeignKey(consumo_promedio,null=False,blank=False)
	Capacidad_Digitos = models.CharField(max_length=15,null=False,blank=False)
	marca_medidor = models.ForeignKey(marca_medidor,null=False,blank=False)
	sector = models.CharField(max_length=45,null=False,blank=False)
	ruta = models.CharField(max_length=45,null=False,blank=False)
	folio = models.CharField(max_length=20,null=False,blank=False)
	lectura = models.CharField(max_length=6,null=False,blank=False)
	iva = models.BooleanField(default=False)
	status = models.BooleanField(default=True)


	def __unicode__(self):
		return self.Nombre

