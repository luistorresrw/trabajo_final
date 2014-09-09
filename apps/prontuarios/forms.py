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