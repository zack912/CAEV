from django import forms
from .models import tipo_movimiento

class tipo_movimientoForm(forms.ModelForm):
	class Meta:
		model = tipo_movimiento
		fields = "__all__"