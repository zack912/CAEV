from django.db import models


class consumo_promedio(models.Model):
	nombre = models.CharField(max_length=5,null=False,blank=False)
	def __unicode__(self):
		return self.nombre