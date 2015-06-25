from django import forms
from .models import marca_medidor

class marca_medidorForm(forms.ModelForm):
	class Meta:
		model = marca_medidor
		fields = "__all__"