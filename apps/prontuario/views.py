from django.shortcuts import render_to_response
from django.template import Context, Template, RequestContext
from django.core.context_processors import csrf 
from trabajo_final.forms import *

def login_ok(request):
	matriz = {
		1:['A','O','U'],
		2:['H','M','Z'],
		3:['S','D','L'],
		4:['V','N','G'],
		5:['B','J','R'],
		6:['F','K','X'],
		7:['T','I','P'],
		8:['W','E','N'],
		9:['C','Q','Y'],
	}
 
	keys = matriz.keys()
	values = matriz.values()
	return render_to_response('varios/login_ok.html', {'matriz':matriz, 'keys':keys,'values':values}, 
		context_instance = RequestContext(request))
	