from django import forms
from .models import Pagos

class PagosForm(forms.ModelForm):
	No_Recibo = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
	Lect_Anterior = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
	Lect_Actual = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
	Consumo_M3 = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
	Meses_Rezago =  forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
	Importe = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
	Fecha_Pago = forms.DateField(widget=forms.TextInput(attrs={'class':'form-control'}))
	Total_Pagar = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
	class Meta:
		model = Pagos
		exclude = {'Cliente',
					}