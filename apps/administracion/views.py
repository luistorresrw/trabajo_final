# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import Context, Template, RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf 
from apps.prontuarios.forms import *
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
  if request.method =="POST": 
      form = PaisesForm(request.POST)
      pais = request.POST.get('descripcion')
      if not pais:
            errors.append('Ingrese pais')
      else:
               if not(len(pais)>=4 and len(pais)< 45):
                     errors.append('El dato ingresado debe tener entre 4 y 45 caracteres')
               else:
                       if form.is_valid():
                        form.save()
                        lista = RefPaises.objects.all()
                        return HttpResponseRedirect('.')   
                       else:
                         errors.append('El Pais que Ud. intenta grabar ya existe') 

      form = PaisesForm()
      lista = RefPaises.objects.all()
      return render_to_response('./paises.html',{'form':form,'lista':lista,'clase':clase,"columns":columns},context_instance=RequestContext(request))
  else:  

     form = PaisesForm()
     lista = RefPaises.objects.all()
     return render_to_response('administracion/paises.html',{'form':form,'lista':lista,'clase':clase,"columns":columns},context_instance=RequestContext(request))

def edit_pais(request,pais):
  pass

def remove_pais(request,pais):
  pass
