from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import Context, Template, RequestContext
from django.core.context_processors import csrf
from trabajo_final.forms import *


def home(request):
	login = LoginForm()
	if request.method == 'POST':
		login = LoginForm(request.POST)
		if login.is_valid():	
			usuario = login.data['usuario']
			password = login.cleaned_data['password']
			user = auth.authenticate(username = usuario, password = password)
			if user is not None and user.is_active:
				request.session['usuario'] = usuario
				request.session['password'] = password
				return HttpResponseRedirect('prontuario/')			 

	values = {
		'login':login,
		'recpass':RecPassForm(),
		
	}
	return render_to_response('varios/login.html', values, context_instance = RequestContext(request))   

