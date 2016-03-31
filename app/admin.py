# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from import_export import fields,widgets
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from import_export.admin import ImportMixin, ExportMixin
from django.contrib.admin import DateFieldListFilter
from import_export import resources, fields

from import_export import resources
from .models import City, Airport, Country
class PlaceWidget(widgets.ForeignKeyWidget):
	def clean(self, value):
		print value
		return self.model.objects.get_or_create(name = value,continent = value )[0]
class PlaceWidget1(widgets.ForeignKeyWidget):
	def clean(self, value):
		return self.model.objects.get_or_create(continent = value)[0]
    
class Placeresources(resources.ModelResource):
	#city = fields.Field(column_name='city', attribute='city', widget=PlaceWidget(City, 'name'))
	country = fields.Field(column_name='country', attribute='country', widget=PlaceWidget(Country, 'name'))
	#continent = fields.Field(column_name='continent', attribute='continent', widget=PlaceWidget(Country, 'continent'))
	name = fields.Field(attribute='name',column_name='name')
	class Meta:		
		model = Airport
		fields = ('name','country','oon','iata','ngrad', 'nmin', 'wgrad', 'wmin', 'typetime')
		export_order = fields
		skip_unchanged = True
        report_skipped = False

	def get_instance(self, instance_loader, row):
		# Returning False prevents us from looking in the
		# database for rows that already exist
		return False

class AirportAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = Placeresources
    fieldsets = [
        ('name', {'fields':['name']}),
        ('city', {'fields':['city']}),
        ('country', {'fields':['country']}),
        ('iata', {'fields':['iata']}),
        ('oon', {'fields':['oon']}),
        ('ngrad', {'fields':['ngrad']}),
        ('nmin', {'fields':['nmin']}),
        ('wgrad', {'fields':['wgrad']}),
        ('wmin', {'fields':['wmin']}),
        ('typetime', {'fields':['typetime']}),
    ]
admin.site.register(Airport, AirportAdmin)
admin.site.register(Country)
admin.site.register(City)
