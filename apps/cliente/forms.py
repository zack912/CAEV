from django import forms
from .models import Cliente
from apps.cat.tipo_usuario.models import tipo_usuario
from apps.cat.tipo_servicio.models import tipo_servicio
from apps.cat.diametro_toma.models import diametro_toma
from apps.cat.consumo_promedio.models import consumo_promedio
from apps.cat.marca_medidor.models import marca_medidor


class ClienteForm(forms.ModelForm):
	
	class Meta:
		model = Cliente
		fields ="__all__"