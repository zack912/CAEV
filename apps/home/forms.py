from django import forms
from django.forms.widgets import PasswordInput,TextInput

class loginForm(forms.Form):
	username = forms.CharField(label="Nombre del usuario",
			widget=TextInput(
			attrs={'class':'username','placeholder':'Escribe tu nombre de usuario'}
				))
	password = forms.CharField(label="Contrasenia",
			widget=PasswordInput(
			attrs={'class':'password','placeholder':'Escribe tu password'}
				))