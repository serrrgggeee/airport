# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
import datetime

class Location(models.Model):
    name = models.CharField('russia name', max_length=100)
    ename = models.CharField('english name', max_length=100)
    iata = models.CharField('iata', max_length=100)
    oon = models.CharField('oon', max_length=100)
    typelocation = models.CharField('typelocation', max_length=100)
    ngrad = models.IntegerField(blank=True, null=True)
    nmin = models.IntegerField(blank=True, null=True)
    wgrad = models.IntegerField(blank=True, null=True)
    wmin = models.IntegerField(blank=True, null=True)
    typetime = models.CharField('typetime', max_length=100)
   
    class Meta:
        abstract = True

class City(models.Model):
	name = models.CharField('russia name', max_length=100)
	ename = models.CharField('english name', max_length=100)
	def __unicode__(self):
		return self.name

class Country(models.Model):
	name = models.CharField('russia name', max_length=100)
	ename = models.CharField('english name', max_length=100)
	continent = models.CharField('continent', max_length=100)
	def __unicode__(self):
		return self.name

class Airport(Location):
	city = models.ForeignKey(City, related_name='city',  blank=True, null=True)
	country = models.ForeignKey(Country, related_name='country', blank=True, null=True)
	now = datetime.datetime.now()
	slug = models.CharField(max_length=150,  default=now)
        

	def __unicode__(self):
		return self.name

