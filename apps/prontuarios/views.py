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


def prontuarios_home(request):
	
	return render_to_response('accounts/logueado.html', {}, context_instance = RequestContext(request))