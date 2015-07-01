from django import forms
from .models import tipo_servicio

class tipo_servicioForm(forms.ModelForm):
	class Meta:
		model = tipo_servicio
		fields = "__all__"