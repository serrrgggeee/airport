#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import 	PlaceList, PlaceDetail

#from django.conf.urls import *
#from django.contrib import admin

urlpatterns=[
	url(r'^(?P<place>airport|city|country)/(?P<pk>[-\w]+)/$',PlaceDetail.as_view(), name='place'),
	url(r'^(?P<place>airport|city|country)/',PlaceList.as_view(), name='places'),
	
   
]
