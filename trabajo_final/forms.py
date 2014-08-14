from django import forms
from django.contrib.auth.models import User 
from django.contrib import auth
from django.utils.translation import ugettext_lazy as _ 

class LoginForm(forms.Form):
	usuario  = forms.IntegerField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Usuario'})))
	password = forms.CharField(widget=forms.PasswordInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Password'},render_value=False)))

class RecPassForm(forms.Form):
	email = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Em@il'})))

class ChangePassForm(forms.Form):
	password_actual	 = forms.CharField(widget=forms.PasswordInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Password actual'},render_value=False)))
	nuevo_password 	 = forms.CharField(widget=forms.PasswordInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Nuevo password'},render_value=False)))
	repetir_password = forms.CharField(widget=forms.PasswordInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Repetir password'},render_value=False)))

#validar formulario django 