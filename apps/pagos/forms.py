from django import forms
from .models import Pagos
from apps.cat.concepto_pago.models import concepto_pago


class PagosForm(forms.ModelForm):
	No_Recibo = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
	Lect_Anterior = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
	Lect_Actual = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
	Consumo_M3 = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
	Meses_Rezago =  forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
	#Importe = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
	Fecha_Pago = forms.DateField(widget=forms.TextInput(attrs={'class':'form-control'}))
	Total_Pagar = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
	class Meta:
		model = Pagos
		exclude = {'Cliente','Importe'
					}



class formCPago(forms.Form):
	mods = (("1","Ajuste"),
			("2","Correcion"),
			("3","Pago de ductos"),
			) 
	pago = forms.ModelChoiceField(queryset=concepto_pago.objects.all())
	importe  = forms.CharField()
	movimiento  = forms.CharField(widget=forms.Select(choices=mods))
	importe_modificacion  = forms.CharField()
