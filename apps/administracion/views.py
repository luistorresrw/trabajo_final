# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import Context, Template, RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf 
from apps.prontuarios.forms import PaisesForm,ProvinciasForm,DepartamentosForm,CiudadesForm,UnidadesForm,DependenciasForm,OcupacionForm,SexoForm,TipoDocumentoForm, EstadoCivilForm
from apps.prontuarios.models import RefPaises,RefProvincia,RefDepartamentos,RefCiudades,UnidadesRegionales,Dependencias,RefOcupacion,RefSexo,RefTipoDocumento,RefEstadosciv

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
  if request.method == 'POST':
    form = PaisesForm(request.POST)
    if form.is_valid():
      pais.descripcion = form.cleaned_data['descripcion']
      pais.save()
      form = PaisesForm()
      pais = RefPaises()
  lista = RefPaises.objects.all()
  tbody = {}
  for elemento in lista:
      tbody[elemento.id] = '<td>'+elemento.descripcion+'</td>'
  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def edit_pais(request,pais):
  clase = "pais"
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
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.descripcion+'</td>'
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
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.descripcion+'</td>'

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
      provincia.pais = form.cleaned_data['pais']
      provincia.descripcion = form.cleaned_data['descripcion']
      provincia.save()
      form = ProvinciasForm()
      provincia = RefProvincia()

  lista = RefProvincia.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.pais.descripcion+'</td><td>'+elemento.descripcion+'</td>'
      

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
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.pais.descripcion+'</td><td>'+elemento.descripcion+'</td>'
  
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
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.pais.descripcion+'</td><td>'+elemento.descripcion+'</td>'
  
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
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.provincia.descripcion+'</td><td>'+elemento.descripcion+'</td>'
  
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
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.provincia.descripcion+'</td><td>'+elemento.descripcion+'</td>'
  
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
 
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.provincia.descripcion+'</td><td>'+elemento.descripcion+'</td>'
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
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.pais.descripcion+'</td><td>'+elemento.provincia.descripcion+'</td><td>'+elemento.descripcion+'</td>'
  
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
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.pais.descripcion+'</td><td>'+elemento.provincia.descripcion+'</td><td>'+elemento.descripcion+'</td>'
  
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
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.pais.descripcion+'</td><td>'+elemento.provincia.descripcion+'</td><td>'+elemento.descripcion+'</td>'
  
  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'ciudad':ciudad,'tbody':tbody},context_instance=RequestContext(request))  


@login_required
def unidad(request):
  clase = "unidad"
  columns = ["ciudad","descripcion"]
  unidad = UnidadesRegionales()
  form = UnidadesForm()
  if request.method == 'POST':
    form = UnidadesForm(request.POST)
    if form.is_valid():
      unidad.ciudad         = form.cleaned_data['ciudad']
      unidad.descripcion    = form.cleaned_data['descripcion']
      unidad.save()
      form = UnidadesForm()
      unidad = UnidadesRegionales()

  lista = UnidadesRegionales.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.ciudad.descripcion+'</td><td>'+elemento.descripcion+'</td>'
  
  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'unidad':unidad,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def edit_unidad(request,id):
  clase = "unidad"
  columns = ["ciudad","descripcion"]
  unidad = UnidadesRegionales.objects.get(id=id)
  form = UnidadesForm(instance=unidad)
  if request.method == 'POST':
    form = UnidadesForm(request.POST)
    if form.is_valid():
      unidad.ciudad         = form.cleaned_data['ciudad']
      unidad.descripcion    = form.cleaned_data['descripcion']
      unidad.save()
      form = UnidadesForm()
      unidad = UnidadesRegionales()

  lista = UnidadesRegionales.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.ciudad.descripcion+'</td><td>'+elemento.descripcion+'</td>'
  
  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'unidad':unidad,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def remove_unidad(request,id):
  clase = "unidad"
  columns = ["ciudad","descripcion"]
  unidad = UnidadesRegionales.objects.get(id=id)
  try:
     unidad.delete()
  except Exception, e:
     raise e 
  form = UnidadesForm()
  unidad = UnidadesRegionales()
  lista = UnidadesRegionales.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.ciudad.descripcion+'</td><td>'+elemento.descripcion+'</td>'
  
  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'unidad':unidad,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def dependencia(request):
  clase = "dependencia"
  columns = ["unidad regional","ciudad","descripcion"]
  dependencia = Dependencias()
  form = DependenciasForm()
  if request.method == 'POST':
    form = DependenciasForm(request.POST)
    if form.is_valid():
      dependencia.unidades_regionales = form.cleaned_data['unidades_regionales']
      dependencia.ciudad              = form.cleaned_data['ciudad']
      dependencia.descripcion         = form.cleaned_data['descripcion']
      dependencia.save()
      form = DependenciasForm()
      dependencia = Dependencias()

  lista = Dependencias.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.unidades_regionales.descripcion+'</td><td>'+elemento.ciudad.descripcion+'</td><td>'+elemento.descripcion+'</td>'
  
  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'dependencia':dependencia,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def edit_dependencia(request,id):
  clase = "dependencia"
  columns = ["unidad regional","ciudad","descripcion"]
  dependencia = Dependencias.objects.get(id=id)
  form = DependenciasForm(instance=dependencia)
  if request.method == 'POST':
    form = DependenciasForm(request.POST)
    if form.is_valid():
      dependencia.unidades_regionales = form.cleaned_data['unidades_regionales']
      dependencia.ciudad              = form.cleaned_data['ciudad']
      dependencia.descripcion         = form.cleaned_data['descripcion']
      dependencia.save()
      form = DependenciasForm()
      dependencia = Dependencias()

  lista = Dependencias.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.unidades_regionales.descripcion+'</td><td>'+elemento.ciudad.descripcion+'</td><td>'+elemento.descripcion+'</td>'
  
  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'dependencia':dependencia,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def remove_dependencia(request,id):
  clase = "dependencia"
  columns = ["unidad regional","ciudad","descripcion"]
  dependencia = Dependencias.objects.get(id=id)
  try:
     dependencia.delete()
  except Exception, e:
     raise e 
  form = DependenciasForm()
  dependencia = Dependencias()
  lista = Dependencias.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.unidades_regionales.descripcion+'</td><td>'+elemento.ciudad.descripcion+'</td><td>'+elemento.descripcion+'</td>'
  
  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'dependencia':dependencia,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def profesion(request):
  clase = "profesion"
  columns = ["descripcion"]
  profesion = RefOcupacion()
  form = OcupacionForm()
  if request.method == 'POST':
    form = OcupacionForm(request.POST)
    if form.is_valid():
      profesion.descripcion    = form.cleaned_data['descripcion']
      profesion.save()
      form = OcupacionForm()
      profesion = RefOcupacion()

  lista = RefOcupacion.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.descripcion+'</td>'
  
  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'profesion':profesion,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def edit_profesion(request,id):
  clase = "profesion"
  columns = ["descripcion"]
  profesion = RefOcupacion.objects.get(id=id)
  form = OcupacionForm(instance=profesion)
  if request.method == 'POST':
    form = OcupacionForm(request.POST)
    if form.is_valid():
      profesion.descripcion    = form.cleaned_data['descripcion']
      profesion.save()
      form = OcupacionForm()
      profesion = RefOcupacion()

  lista = RefOcupacion.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.descripcion+'</td>'
  
  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'profesion':profesion,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def remove_profesion(request,id):
  clase = "profesion"
  columns = ["descripcion"]
  profesion = RefOcupacion.objects.get(id=id)
  try:
     profesion.delete()
  except Exception, e:
     raise e 
  profesion = RefOcupacion()
  form = OcupacionForm()
  lista = RefOcupacion.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.descripcion+'</td>'
  
  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'profesion':profesion,'tbody':tbody},context_instance=RequestContext(request))


@login_required
def sexo(request):
  clase = "sexo"
  columns = ["descripcion"]
  sexo = RefSexo()
  form = SexoForm()
  if request.method =="POST": 
    
    form = SexoForm(request.POST)
    if form.is_valid():
      sexo.descripcion = form.cleaned_data['descripcion']
      sexo.save()
      form = SexoForm()
      sexo = RefSexo()
  
  lista = RefSexo.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.descripcion+'</td>'
  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'tbody':tbody},context_instance=RequestContext(request))


@login_required
def edit_sexo(request,sexo):
  clase="sexo"
  columns = ["descripcion"]
  sexo = RefSexo.objects.get(id=sexo)
  form = SexoForm(instance=sexo)
  if request.method == 'POST':

    form = SexoForm(request.POST)
    if form.is_valid():
      sexo.descripcion = form.cleaned_data['descripcion'];
      sexo.save()
      form = SexoForm()
      sexo = RefSexo()

  lista = RefSexo.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.descripcion+'</td>'
  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'sexo':sexo,'tbody':tbody},context_instance=RequestContext(request))  

@login_required
def remove_sexo(request,sexo):
  clase="sexo"
  columns = ["descripcion"]
  sexo = RefSexo.objects.get(id=sexo)
  try:
     sexo.delete()
  except Exception, e:
     raise e 
  form = SexoForm()
  sexo = RefSexo()
  lista = RefSexo.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.descripcion+'</td>'

  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'sexo':sexo,'tbody':tbody},context_instance=RequestContext(request))  


@login_required
def tipo_doc(request):
  clase = "tipo_doc"
  columns = ["descripcion"]
  tipo_doc = RefTipoDocumento()
  form = TipoDocumentoForm()
  if request.method =="POST": 
      form = TipoDocumentoForm(request.POST)
      if form.is_valid():
        tipo_doc.descripcion = form.cleaned_data['descripcion']
        tipo_doc.save()
        form = TipoDocumentoForm()
        tipo_doc = RefTipoDocumento()
  
  lista = RefTipoDocumento.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.descripcion+'</td>'
  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'tbody':tbody},context_instance=RequestContext(request))



@login_required
def edit_tipo_doc(request,tipo_doc):
  clase="tipo_doc"
  columns = ["descripcion"]
  tipo_doc = RefTipoDocumento.objects.get(id=tipo_doc)
  form = TipoDocumentoForm(instance=tipo_doc)
  if request.method == 'POST':
    form = TipoDocumentoForm(request.POST)
    if form.is_valid():
      tipo_doc.descripcion = form.cleaned_data['descripcion'];
      tipo_doc.save()
      form = TipoDocumentoForm()
      tipo_doc = RefTipoDocumento()

  lista = RefTipoDocumento.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.descripcion+'</td>'
  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'tipo_doc':tipo_doc,'tbody':tbody},context_instance=RequestContext(request))  

@login_required
def remove_tipo_doc(request,tipo_doc):
  clase="tipo_doc"
  columns = ["descripcion"]
  tipo_doc = RefTipoDocumento.objects.get(id=tipo_doc)
  try:
     tipo_doc.delete()
  except Exception, e:
     raise e 
  form = TipoDocumentoForm()
  tipo_doc = RefTipoDocumento()
  lista = RefTipoDocumento.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.descripcion+'</td>'

  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'tipo_doc':tipo_doc,'tbody':tbody},context_instance=RequestContext(request))    



@login_required
def estado_civil(request):
  clase = "estado_civil"
  columns = ["descripcion"]
  estado_civil = RefEstadosciv()
  form = EstadoCivilForm()
  if request.method =="POST": 
      form = EstadoCivilForm(request.POST)
      if form.is_valid():
        estado_civil.descripcion = form.cleaned_data['descripcion']
        estado_civil.save()
        form = EstadoCivilForm()
        estado_civil = RefEstadosciv()
  
  lista = RefEstadosciv.objects.all()
  tbody = {}

  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.descripcion+'</td>'
  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def edit_estado_civil(request,estado_civil):
  clase="estado_civil"
  columns = ["descripcion"]
  estado_civil = RefEstadosciv.objects.get(id=estado_civil)
  form = EstadoCivilForm(instance=estado_civil)
  if request.method == 'POST':
    form = EstadoCivilForm(request.POST)
    if form.is_valid():
      estado_civil.descripcion = form.cleaned_data['descripcion'];
      estado_civil.save()
      form = EstadoCivilForm()
      estado_civil = RefEstadosciv()

  lista = RefEstadosciv.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.descripcion+'</td>'
  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'estado_civil':estado_civil,'tbody':tbody},context_instance=RequestContext(request))  
  
@login_required
def remove_estado_civil(request,estado_civil):
  clase="estado_civil"
  columns = ["descripcion"]
  estado_civil = RefEstadosciv.objects.get(id=estado_civil)
  try:
     estado_civil.delete()
  except Exception, e:
     raise e 
  form = EstadoCivilForm()
  estado_civil = RefEstadosciv()
  lista = RefEstadosciv.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.descripcion+'</td>'

  return render_to_response('administracion/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'estado_civil':estado_civil,'tbody':tbody},context_instance=RequestContext(request))    

