from django.db import models

class marca_medidor(models.Model):
	nombre = models.CharField(max_length=100,null=False,blank=False)
	#status = models.BooleanField(default=True)
	def __unicode__(self):
		return self.nombre