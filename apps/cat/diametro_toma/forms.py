from django import forms
from .models import diametro_toma

class diametro_tomaForm(forms.ModelForm):
	class Meta:
		model = diametro_toma
		fields = "__all__"

