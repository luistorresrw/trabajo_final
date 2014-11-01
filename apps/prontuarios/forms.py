# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User 
from django.contrib import auth
from django.utils.translation import ugettext_lazy as _ 
from models import *


class PaisesForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Nombre del Pais','autocomplete':'off'})), required=True)
    
    class Meta:
		model = RefPaises
        
class ProvinciasForm(forms.ModelForm):
    pais 		= forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})),queryset=RefPaises.objects.all(),required=True)
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Nombre de la Provincia','autocomplete':'off'})),required=True)
   
    class Meta:
        model = RefProvincia

class DepartamentosForm(forms.ModelForm):
	provincia 	= forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})),queryset=RefProvincia.objects.filter(pais=RefPaises.objects.filter(descripcion__contains="ARGENTINA").values('id')))
	descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Nombre del Departamento','autocomplete':'off'})),required=True)

	class Meta:
		model = RefDepartamentos

class CiudadesForm(forms.ModelForm):
	pais 			= forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})),queryset=RefPaises.objects.all())
	provincia 		= forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})),queryset=RefProvincia.objects.all(),required=False)
	departamento    = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})),queryset=RefDepartamentos.objects.all(),required=False)
	descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Nombre de la ciudad','autocomplete':'off'})),required=True)

	class Meta:
		model = RefCiudades
		exclude = ('lat','longi',)

class UnidadesForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Nombre de la unidad','autocomplete':'off'})),required=True)
    ciudad = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})), queryset= RefCiudades.objects.filter(provincia = RefProvincia.objects.filter(descripcion__contains = 'CHUBUT').values('id'))  )
    class Meta:
        model = UnidadesRegionales

class DependenciasForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Nombre de la dependencia','autocomplete':'off'})),required=True)
    ciudad = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})), queryset= RefCiudades.objects.filter(provincia = RefProvincia.objects.filter(descripcion__contains = 'CHUBUT').values('id'))  )
    unidades_regionales = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})), queryset= UnidadesRegionales.objects.all())

    class Meta:
        model = Dependencias 

class OcupacionForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Ocupación / Profesión / Oficio','autocomplete':'off'})),required=True)
    class Meta:
        model = RefOcupacion


class SexoForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Sexo','autocomplete':'off'})),required=True)
    class Meta:
        model = RefSexo

class TipoDocumentoForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Tipo de documento','autocomplete':'off'})),required=True)
    class Meta:
        model = RefTipoDocumento 

class EstadoCivilForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Estado civil','autocomplete':'off'})),required=True)
    class Meta:
        model = RefEstadosciv 
        

   
