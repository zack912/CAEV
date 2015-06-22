from django.db import models


class concepto_pago(models.Model):
	concepto = models.CharField(max_length=100,null=False,blank=False)
	def __unicode__(self):
		return self.concepto