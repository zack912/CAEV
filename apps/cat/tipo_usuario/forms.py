from django import forms
from .models import tipo_usuario

class tipo_usuarioForm(forms.ModelForm):
	class Meta:
		model = tipo_usuario
		fields = "__all__"