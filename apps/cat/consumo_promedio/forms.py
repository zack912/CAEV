from django import forms
from .models import consumo_promedio

class consumo_promedioForm(forms.ModelForm):
	class Meta:
		model = consumo_promedio
		fields = "__all__"
