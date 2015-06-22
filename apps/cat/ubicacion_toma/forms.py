from django import forms
from .models import ubicacion_toma


class ubicacion_tomaForm(forms.ModelForm):
	class Meta:
		model = ubicacion_toma
		fields = "__all__"