# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import Context, Template, RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf 
from apps.accounts.forms import *
from datetime import date
import random
from django.contrib.auth import *




def home(request):
	login = LoginForm()
	recpass = RecPassForm()
	mensaje = ""
	if request.method == 'POST':
		login = LoginForm(request.POST)
		if login.is_valid():	
			usuario = login.data['usuario']
			password = login.cleaned_data['password']
			user = auth.authenticate(username = usuario, password = password)
			if user is not None and user.is_active:
				request.session['usuario'] = usuario
				request.session['password'] = password
				return HttpResponseRedirect('accounts/')
			else:
				login = LoginForm()
				mensaje = "Usuario y/o contraseña incorrectos."


	values = {
		'recpass':recpass,
		'login':login,
		'mensaje':mensaje,
	}
	return render_to_response('accounts/login.html', values, context_instance = RequestContext(request))  


def login_ok(request):
	if request.method == 'POST':
		input_pil = request.POST['pil']
		usuario = request.session['usuario']
		password = request.session['password']
		user = auth.authenticate(username = usuario, password = password)
		primer_logueo = user.profile.primer_logueo
		print primer_logueo
		if user is not None and user.is_active and verificar_matriz(request,input_pil,user) and primer_logueo == True:
			form = ChangePassForm()
			request.session['user'] = user.username
			return render_to_response('accounts/change_pass.html', {'form':form,}, context_instance = RequestContext(request))
		if user is not None and user.is_active and verificar_matriz(request,input_pil,user) and primer_logueo == False:
			return HttpResponseRedirect('../prontuarios/')
			
	matriz = matrix()
	request.session['matriz'] = matriz
 	keys = matriz.keys()
	values = matriz.values()
	return render_to_response('accounts/login_ok.html', {'matriz':matriz, 'keys':keys,'values':values}, context_instance = RequestContext(request))
	

def matrix():
	alpha = [u'A',u'B',u'C',u'D',u'E',u'F',u'G',u'H',u'I',u'J',u'K',u'L',u'M',u'N',u'Ñ',u'O',u'P',u'Q',u'R',u'S',u'T',u'U',u'V',u'W',u'X',u'Y',u'Z']
	matriz = {
		1:[],
		2:[],
		3:[],
		4:[],
		5:[],
		6:[],
		7:[],
		8:[],
		9:[],
	}
	for k in matriz.keys():
		for x in range(3):
			matriz[k].append(get_value(alpha))
		matriz[k] = u''.join(matriz[k])
	return matriz

def get_value(alpha):
	if len(alpha)==1:
		indice = 0
	else:
		indice = random.randrange(0,len(alpha))
	valor = alpha[indice]
	alpha.remove(valor)
	return valor

def verificar_matriz(request,input_pil,user):
	if input_pil and input_pil != "":
		matriz = request.session['matriz']
		pil = user.profile.pil
		grupo1 = matriz[input_pil[0]]
		grupo2 = matriz[input_pil[1]]
		grupo3 = matriz[input_pil[2]]
		veri1 = pil[0] in grupo1
		veri2 = pil[1] in grupo2
		veri3 = pil[2] in grupo3
		return veri1 and veri2 and veri3
	return False
	
def change_password(request):
	if request.method == 'POST':
		form = ChangePassForm(request.POST)

		if form.is_valid():
			username = request.session['user']
			password = form.data['password_actual']
			user = auth.authenticate(username=username, password=password)
			
			


			if user is None:
				return HttpResponseRedirect(reverse('home'))
			else:
				nuevo_password = form.cleaned_data['nuevo_password']
				user.set_password(nuevo_password)
				try:
					user.save()
					profile = user.profile
					profile.primer_logueo = False
					profile.fecha_ultimo_cambio = date.today()
					print user.profile
					profile.save()
				except Exception, e:
					raise e
					
				return HttpResponseRedirect('prontuarios/')
				
	return HttpResponseRedirect(reverse('home'))

def cerrar_sesion(request):
	logout(request)
	return HttpResponseRedirect(reverse('home'))


