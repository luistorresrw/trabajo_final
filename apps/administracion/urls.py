#! /usr/bin/python	
# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from views import *


urlpatterns = patterns('',
	url(r'^$', admin_home, name = 'admin_home'),
	url(r'^pais/$',  pais, name='pais'),
	url(r'^edit_pais/(?P<pais>[0-9A-Za-z]+)/$', edit_pais ,name='edit_pais'),
	url(r'^remove_pais/(?P<pais>[0-9A-Za-z]+)/$', remove_pais ,name='remove_pais'),
) 
