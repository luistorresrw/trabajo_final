# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import Context, Template, RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf 
from apps.prontuarios.forms import PaisesForm
from apps.prontuarios.models import RefPaises
from datetime import date
import random
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required


@login_required
def admin_home(request):
	
	return render_to_response('administracion/logueado_admin.html', {}, context_instance = RequestContext(request))


@login_required
def pais(request):
  clase = "pais"
  columns = ["descripcion"]
  destino = "edit"
  pais = RefPaises()
  print request.method
  if request.method =="POST": 
      form = PaisesForm(request.POST)
      print form.is_valid
      if form.is_valid():
        pais.descripcion = form.cleaned_data['descripcion']
        pais.save()
        form = PaisesForm()
        lista = RefPaises.objects.all()
      return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns},context_instance=RequestContext(request))
  else:  

     form = PaisesForm()
     lista = RefPaises.objects.all()
     return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns},context_instance=RequestContext(request))

def edit_pais(request,pais):
  pass

def remove_pais(request,pais):
  pass
