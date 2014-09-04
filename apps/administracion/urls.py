#! /usr/bin/python	
# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from views import *


urlpatterns = patterns('',
	url(r'^$', admin_home, name = 'admin_home'),
	url(r'^pais/$',  pais, name='pais'),
) 
