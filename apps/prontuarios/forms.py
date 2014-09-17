# -*- encoding: utf-8 -*-
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
	provincia 		= forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})),queryset=RefProvincia.objects.all(),required=False)
	departamento    = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})),queryset=RefDepartamentos.objects.all(),required=False)
	descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Nombre de la ciudad','required':'required','autocomplete':'off'})),required=True)

	class Meta:
		model = RefCiudades
		exclude = ('lat','longi',)

class UnidadesForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Nombre de la unidad','required':'required','autocomplete':'off'})),required=True)
    ciudad = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})), queryset= RefCiudades.objects.filter(provincia = RefProvincia.objects.filter(descripcion__contains = 'CHUBUT').values('id'))  )
    class Meta:
        model = UnidadesRegionales

class DependenciasForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Nombre de la dependencia','required':'required','autocomplete':'off'})),required=True)
    ciudad = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})), queryset= RefCiudades.objects.filter(provincia = RefProvincia.objects.filter(descripcion__contains = 'CHUBUT').values('id'))  )
    unidades_regionales = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})), queryset= UnidadesRegionales.objects.all())

    
    class Meta:
        model = Dependencias 

class OcupacionForm(forms.ModelForm):

    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Ocupación / Profesión / Oficio','required':'required','autocomplete':'off'})),required=True)
    class Meta:
        model = RefOcupacion


class SexoForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Sexo','required':'required'})),required=True)
    class Meta:
        model = RefSexo

class TipoDocumentoForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Tipo de documento','required':'required'})),required=True)
    class Meta:
        model = RefTipoDocumento 

class EstadoCivilForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Estado civil','required':'required'})),required=True)
    class Meta:
        model = RefEstadosciv 

   