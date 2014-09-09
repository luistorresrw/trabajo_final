# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import Context, Template, RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf 
from apps.prontuarios.forms import PaisesForm,ProvinciasForm,DepartamentosForm,CiudadesForm
from apps.prontuarios.models import RefPaises,RefProvincia,RefDepartamentos,RefCiudades
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

@login_required
def departamento(request):
  clase = "departamento"
  columns = ["provincia","descripcion"]
  departamento = RefDepartamentos()
  form = DepartamentosForm()
  if request.method == 'POST':
    form = DepartamentosForm(request.POST)
    print form
    if form.is_valid():
      departamento.provincia   = form.cleaned_data['provincia']
      departamento.descripcion = form.cleaned_data['descripcion']
      departamento.save()
      form = DepartamentosForm()
      departamento = RefDepartamentos()

  lista = RefDepartamentos.objects.all()
  tbody = []
  for elemento in lista:
      fila = '<td>'+elemento.provincia.descripcion+'</td><td>'+elemento.descripcion+'</td>'
      tbody.append(fila)
  
  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'departamento':departamento,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def edit_departamento(request,dto):
  clase="departamento"
  columns = ["provincia","descripcion"]
  departamento = RefDepartamentos.objects.get(id=dto)
  form = DepartamentosForm(instance=departamento)
  if request.method == 'POST':
    form = DepartamentosForm(request.POST)
    if form.is_valid():
      departamento.provincia   = form.cleaned_data['provincia'];
      departamento.descripcion = form.cleaned_data['descripcion']
      departamento.save()
      form = DepartamentosForm()
      departamento = RefDepartamentos()

  lista = RefDepartamentos.objects.all()
  tbody = []
  for elemento in lista:
      fila = '<td>'+elemento.provincia.descripcion+'</td><td>'+elemento.descripcion+'</td>'
      tbody.append(fila)
  
  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'departamento':departamento,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def remove_departamento(request,dto):
  clase="departamento"
  columns = ["provincia","descripcion"]
  departamento = RefDepartamentos.objects.get(id=dto)
  try:
     departamento.delete()
  except Exception, e:
     raise e 
  form = DepartamentosForm()
  departamento = RefDepartamentos()
  lista = RefDepartamentos.objects.all()
  tbody = []
  for elemento in lista:
      fila = '<td>'+elemento.provincia.descripcion+'</td><td>'+elemento.descripcion+'</td>'
      tbody.append(fila)
  
  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'departamento':departamento,'tbody':tbody},context_instance=RequestContext(request))  

@login_required
def ciudad(request):
  clase = "ciudad"
  columns = ["pais","provincia","descripcion"]
  ciudad = RefCiudades()
  form = CiudadesForm()
  if request.method == 'POST':
    form = CiudadesForm(request.POST)
    print form
    if form.is_valid():
      ciudad.pais           = form.cleaned_data['pais']
      ciudad.provincia      = form.cleaned_data['provincia']
      ciudad.departamento   = form.cleaned_data['departamento']
      ciudad.descripcion    = form.cleaned_data['descripcion']
      ciudad.save()
      form = CiudadesForm()
      ciudad = RefCiudades()

  lista = RefCiudades.objects.all()
  tbody = []
  for elemento in lista:
      fila = '<td>'+elemento.pais.descripcion+'</td><td>'+elemento.provincia.descripcion+'</td><td>'+elemento.descripcion+'</td>'
      tbody.append(fila)
  
  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'ciudad':ciudad,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def edit_ciudad(request,cdd):
  clase="ciudad"
  columns = ["pais","provincia","descripcion"]
  ciudad = RefCiudades.objects.get(id=cdd)
  form = CiudadesForm(instance=ciudad)
  if request.method == 'POST':
    form = CiudadesForm(request.POST)
    if form.is_valid():
      ciudad.pais           = form.cleaned_data['pais']
      ciudad.provincia      = form.cleaned_data['provincia']
      ciudad.departamento   = form.cleaned_data['departamento']
      ciudad.descripcion    = form.cleaned_data['descripcion']
      ciudad.save()
      form = CiudadesForm()
      ciudad = RefCiudades()

  lista = RefCiudades.objects.all()
  tbody = []
  for elemento in lista:
      fila = '<td>'+elemento.pais.descripcion+'</td><td>'+elemento.provincia.descripcion+'</td><td>'+elemento.descripcion+'</td>'
      tbody.append(fila)
  
  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'ciudad':ciudad,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def remove_ciudad(request,cdd):
  clase="ciudad"
  columns = ["pais","provincia","descripcion"]
  ciudad = RefCiudades.objects.get(id=cdd)
  try:
     ciudad.delete()
  except Exception, e:
     raise e 
  form = CiudadesForm()
  ciudad = RefCiudades()
  lista = RefCiudades.objects.all()
  tbody = []
  for elemento in lista:
      fila = '<td>'+elemento.pais.descripcion+'</td><td>'+elemento.provincia.descripcion+'</td><td>'+elemento.descripcion+'</td>'
      tbody.append(fila)
  
  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'ciudad':ciudad,'tbody':tbody},context_instance=RequestContext(request))  