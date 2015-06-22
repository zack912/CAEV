from django.db import models

class tipo_movimiento(models.Model):
	tipo = models.CharField(max_length=100)
	def __unicode__(self):
		return self.tipo
