from django import forms
from django.contrib.auth.models import User 
from django.contrib import auth
from django.utils.translation import ugettext_lazy as _ 
from models import *

class PaisesForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Nombre del Pais','required':'required'})),required=True)
    class Meta:
		model = RefPaises

class ProvinciasForm(forms.ModelForm):
    pais 		= forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level','required':'required'})),queryset=RefPaises.objects.all())
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Nombre de la Provincia','required':'required','autocomplete':'off'})),required=True)
   
    class Meta:
        model = RefProvincia

class DepartamentosForm(forms.ModelForm):
	provincia 	= forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level','required':'required'})),queryset=RefProvincia.objects.filter(pais=RefPaises.objects.filter(descripcion__contains="ARGENTINA").values('id')))
	descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Nombre del Departamento','required':'required','autocomplete':'off'})),required=True)

	class Meta:
		model = RefDepartamentos

class CiudadesForm(forms.ModelForm):
	pais 			= forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level','required':'required'})),queryset=RefPaises.objects.all())
	provincia 		= forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})),queryset=RefProvincia.objects.all())
	departamento    = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})),queryset=RefDepartamentos.objects.all())
	descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Nombre de la ciudad','required':'required','autocomplete':'off'})),required=True)

	class Meta:
		model = RefCiudades
		exclude = ('lat','longi',)