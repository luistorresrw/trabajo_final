from django import forms
from django.contrib.auth.models import User 
from django.contrib import auth
from django.utils.translation import ugettext_lazy as _ 
from models import *

class PaisesForm(forms.ModelForm):
    descripcion = forms.CharField(required=True)
    class Meta:
		model = RefPaises