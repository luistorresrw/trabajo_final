#! /usr/bin/python	
# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from views import *


urlpatterns = patterns('',
	url(r'^$', login_ok, name = 'login_ok'),
	url(r'^change_pass/$', change_password, name='change_password'),
	url(r'^cerrar_sesion/$', cerrar_sesion, name='cerrar_sesion'),
) 

