#! /usr/bin/python	
# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from views import *


urlpatterns = patterns('',
	url(r'^$', login_ok, name = 'login_ok'),
	url(r'^change_pass/$', change_password, name='change_password'),
	url(r'^cerrar_sesion/$', cerrar_sesion, name='cerrar_sesion'),
	
	url(r'^user/$', usuarios, name='usuarios'),
	url(r'^edit_user/(?P<id>[0-9A-Za-z]+)/$',  edit_usuarios, name='edit_user'),
	url(r'^remove_user/(?P<id>[0-9A-Za-z]+)/$',  remove_usuarios, name='remove_user'),
	url(r'^obtener_persona/(?P<dni>[0-9]+)/$', obtener_persona, name="obtener_persona"),
) 

