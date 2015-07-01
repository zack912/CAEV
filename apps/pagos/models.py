from django.db import models
from apps.cliente.models import Cliente
import datetime

class Pagos(models.Model):
	"""Datos pagos"""
	tipo_pago = (
			("mensual","Mensual"),
			("anual","Anual"),
			
			)
	concepto_pago = models.CharField(choices=tipo_pago,max_length=15,null=False,blank=False)
	Cliente = models.ForeignKey(Cliente,null=False,blank=False)
	No_Recibo = models.IntegerField(max_length=15,null=False,blank=False)
	Lect_Anterior = models.IntegerField(max_length=15,null=False,blank=False)
	Lect_Actual = models.IntegerField(max_length=15,null=False,blank=False)
	Consumo_M3 = models.IntegerField(max_length=15,null=False,blank=False)
	Meses_Rezago =  models.IntegerField(max_length=8,null=False,blank=False)
	mesfacturacion =  models.CharField(max_length=40,null=False,blank=False)
	Importe = models.IntegerField(max_length=15,null=False,blank=False)
	observaciones= models.CharField(max_length=600,null=False,blank=False)
	Fecha_Pago = models.DateField()
	Total_Pagar = models.IntegerField(max_length=15,null=False,blank=False)
	
	def __unicode__(self):
		return self.Cliente.Nombre

