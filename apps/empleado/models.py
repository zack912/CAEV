from django.db import models


class Empleado(models.Model):
	sexos = (('hombre','Hombre'),('mujer','Mujer'))
	"""Datos del empleado"""
	Nombre = models.CharField(max_length=200,null=False,blank=False)
	Direccion = models.CharField(max_length=200,null=False,blank=False)
	Municipio = models.CharField(max_length=50,null=False,blank=False)
	Telefono = models.CharField(max_length=12,null=False,blank=False)
	Sexo = models.CharField(max_length=20,choices=sexos,blank=False)
	RFC = models.CharField(max_length = 13, null=False,blank=False)
	CURP = models.CharField(max_length=15, null=False,blank=False)
	Departamento = models.CharField(max_length=50,null=False,blank=False)
	Puesto = models.CharField(max_length=50,null=False,blank=False)
	Perfil = models.CharField(max_length=50,null=False,blank=False)
	Nomb_User = models.CharField(max_length=20,null=False,blank=False)
	Contrasenia = models.CharField(max_length=15,null=False,blank=False)
	No_empleado= models.IntegerField(max_length=15,null=False,blank=False)


	def __unicode__(self):
		return self.Nombre
