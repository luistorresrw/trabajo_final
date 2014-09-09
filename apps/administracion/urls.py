#! /usr/bin/python	
# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from views import *


urlpatterns = patterns('',
	url(r'^$', admin_home, name = 'admin_home'),
	url(r'^pais/$',  pais, name='pais'),
	url(r'^edit_pais/(?P<pais>[0-9A-Za-z]+)/$', edit_pais ,name='edit_pais'),
	url(r'^remove_pais/(?P<pais>[0-9A-Za-z]+)/$', remove_pais ,name='remove_pais'),
	url(r'^provincia/$',  provincia, name='provincia'),
	url(r'^edit_provincia/(?P<prov>[0-9A-Za-z]+)/$', edit_provincia ,name='edit_provincia'),
	url(r'^remove_provincia/(?P<prov>[0-9A-Za-z]+)/$', remove_provincia ,name='remove_provincia'),
	url(r'^departamento/$',  departamento, name='departamento'),
	url(r'^edit_departamento/(?P<dto>[0-9A-Za-z]+)/$', edit_departamento ,name='edit_departamento'),
	url(r'^remove_departamento/(?P<dto>[0-9A-Za-z]+)/$', remove_departamento ,name='remove_departamento'),
	url(r'^ciudad/$',  ciudad, name='ciudad'),
	url(r'^edit_ciudad/(?P<cdd>[0-9A-Za-z]+)/$', edit_ciudad ,name='edit_ciudad'),
	url(r'^remove_ciudad/(?P<cdd>[0-9A-Za-z]+)/$', remove_ciudad ,name='remove_ciudad'),
) 
