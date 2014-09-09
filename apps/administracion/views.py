# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import Context, Template, RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf 
from apps.prontuarios.forms import PaisesForm,ProvinciasForm
from apps.prontuarios.models import RefPaises,RefProvincia
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
  pais = RefPaises()
  form = PaisesForm()
  if request.method =="POST": 
      form = PaisesForm(request.POST)
      if form.is_valid():
        pais.descripcion = form.cleaned_data['descripcion']
        pais.save()
        form = PaisesForm()
        pais = RefPaises()
  
  lista = RefPaises.objects.all()
  tbody = []
  for elemento in lista:
      fila = '<td>'+elemento.descripcion+'</td>'
      tbody.append(fila)
  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def edit_pais(request,pais):
  clase="pais"
  columns = ["descripcion"]
  pais = RefPaises.objects.get(id=pais)
  form = PaisesForm(instance=pais)
  if request.method == 'POST':
    form = PaisesForm(request.POST)
    if form.is_valid():
      pais.descripcion = form.cleaned_data['descripcion'];
      pais.save()
      form = PaisesForm()
      pais = RefPaises()

  lista = RefPaises.objects.all()
  tbody = []
  for elemento in lista:
      fila = '<td>'+elemento.descripcion+'</td>'
      tbody.append(fila)
  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'pais':pais,'tbody':tbody},context_instance=RequestContext(request))  

@login_required
def remove_pais(request,pais):
  clase="pais"
  columns = ["descripcion"]
  pais = RefPaises.objects.get(id=pais)
  try:
     pais.delete()
  except Exception, e:
     raise e 
  form = PaisesForm()
  pais = RefPaises()
  lista = RefPaises.objects.all()
  tbody = []
  for elemento in lista:
      fila = '<td>'+elemento.descripcion+'</td>'
      tbody.append(fila)
  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'pais':pais,'tbody':tbody},context_instance=RequestContext(request))  

@login_required
def provincia(request):
  clase = "provincia"
  columns = ["pais","descripcion"]
  provincia = RefProvincia()
  form = ProvinciasForm()
  if request.method == 'POST':
    form = ProvinciasForm(request.POST)
    print form
    if form.is_valid():
      provincia.pais        = form.cleaned_data['pais']
      provincia.descripcion = form.cleaned_data['descripcion']
      provincia.save()
      form = ProvinciasForm()
      provincia = RefProvincia()

  lista = RefProvincia.objects.all()
  tbody = []
  for elemento in lista:
      fila = '<td>'+elemento.pais.descripcion+'</td><td>'+elemento.descripcion+'</td>'
      tbody.append(fila)
  
  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'provincia':provincia,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def edit_provincia(request,prov):
  clase="provincia"
  columns = ["pais","descripcion"]
  provincia = RefProvincia.objects.get(id=prov)
  form = ProvinciasForm(instance=provincia)
  if request.method == 'POST':
    form = ProvinciasForm(request.POST)
    if form.is_valid():
      provincia.pais        = form.cleaned_data['pais'];
      provincia.descripcion = form.cleaned_data['descripcion']
      provincia.save()
      form = ProvinciasForm()
      provincia = RefProvincia()

  lista = RefProvincia.objects.all()
  tbody = []
  for elemento in lista:
      fila = '<td>'+elemento.pais.descripcion+'</td><td>'+elemento.descripcion+'</td>'
      tbody.append(fila)
  
  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'provincia':provincia,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def remove_provincia(request,prov):
  clase="provincia"
  columns = ["pais","descripcion"]
  provincia = RefProvincia.objects.get(id=prov)
  try:
     provincia.delete()
  except Exception, e:
     raise e 
  form = ProvinciasForm()
  provincia = RefProvincia()
  lista = RefProvincia.objects.all()
  tbody = []
  for elemento in lista:
      fila = '<td>'+elemento.pais.descripcion+'</td><td>'+elemento.descripcion+'</td>'
      tbody.append(fila)
  
  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'provincia':provincia,'tbody':tbody},context_instance=RequestContext(request))