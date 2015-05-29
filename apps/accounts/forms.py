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

class UserForm(forms.ModelForm):
	username = forms.CharField(label='Numero de Documento',widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level number_input', 'placeholder':'Numero de documento','autocomplete':'off'},render_value=False)))
	last_name = forms.CharField(label='Apellidos',widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Apellidos','disabled':'disabled'},render_value=False)))
	first_name = forms.CharField(label='Nombres',widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Nombres','disabled':'disabled'},render_value=False)))
	email = forms.EmailField(label='Correo Electronico',widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Email','disabled':'disabled'},render_value=False)))
	is_staff = forms.BooleanField(label="Pertenece al equipo?",required=False,widget=forms.CheckboxInput(attrs=dict({'checked':'checked'})),help_text="Deje seleccionada esta casilla si el usuario es Administrador.")

	class Meta:
		model = User
		exclude = ('last_login','date_joined','password','is_active','groups','user_permissions','is_superuser')
