# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import Context, Template, RequestContext
from django.core.context_processors import csrf 
from trabajo_final.forms import *
import random

def login_ok(request):
	matriz = matrix()
 
	keys = matriz.keys()
	values = matriz.values()
	return render_to_response('varios/principal.html', {'matriz':matriz, 'keys':keys,'values':values}, 
		context_instance = RequestContext(request))
	

def matrix():
	alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
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
	return matriz

def get_value(alpha):
	if len(alpha)==1:
		indice = 0
	else:
		indice = random.randrange(0,len(alpha)-1)
	valor = alpha[indice]
	alpha.remove(valor)
	return valor