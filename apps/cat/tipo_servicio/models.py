from django.db import models

class tipo_servicio(models.Model):
	nombre = models.CharField(max_length=100,null=False,blank=False)
	def __unicode__(self):
		return self.nombre