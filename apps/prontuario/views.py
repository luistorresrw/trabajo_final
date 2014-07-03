# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import Context, Template, RequestContext
from django.core.context_processors import csrf 
from trabajo_final.forms import *
import random

def login_ok(request):
	if request.method == 'POST':
		input_pil = request.POST['pil']
		usuario = request.session['usuario']
		password = request.session['password']
		user = auth.authenticate(username = usuario, password = password)
		if user is not None and user.is_active:
			if verificar_matriz(request,input_pil,user):
				auth.login(request, user)
				return render_to_response('varios/logueado.html', {}, context_instance = RequestContext(request))		


	matriz = matrix()
	request.session['matriz'] = matriz
 	keys = matriz.keys()
	values = matriz.values()
	return render_to_response('varios/login_ok.html', {'matriz':matriz, 'keys':keys,'values':values}, context_instance = RequestContext(request))
	

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
		indice = random.randrange(0,len(alpha)-1)
	valor = alpha[indice]
	alpha.remove(valor)
	return valor

def verificar_matriz(request,input_pil,user):
	matriz = request.session['matriz']
	pil = user.profile.pil
	grupo1 = matriz[int(input_pil[0])]
	grupo2 = matriz[int(input_pil[1])]
	grupo3 = matriz[int(input_pil[2])]
	veri1 = pil[0] in grupo1
	veri2 = pil[1] in grupo2
	veri3 = pil[2] in grupo3
	return veri1 and veri2 and veri3
	