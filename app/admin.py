# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from import_export import fields,widgets, resources
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportActionModelAdmin

from import_export import resources
from .models import City, Airport, Country
class CityWidget(widgets.ForeignKeyWidget):
	def clean(self, value, *args):
		return self.model.objects.get_or_create(name = value)[0]
class Myfield(fields.Field):
	def clean(self, data):
		"""
		Translates the value stored in the imported datasource to an
		appropriate Python object and returns it.
		"""
		a=data.values()
		ecity = a[4]
		ecountry = a[6]
		continent = a[7]
		args =(ecity, ecountry, continent)
		
		try:
			value = data[self.column_name]
		except KeyError:
			raise KeyError("Column '%s' not found in dataset. Available ""columns are: %s" % (self.column_name,list(data.keys())))
		try:
			value = self.widget.clean(value, *args)
		except ValueError as e:
			raise ValueError("Column '%s': %s" % (self.column_name, e))

		if not value and self.default != NOT_PROVIDED:
			if callable(self.default):
				return self.default()
			return self.default
		
		
		return value
        
		
	#continent = 'dfdfdf'
class CountryWidget(widgets.ForeignKeyWidget):
	def clean(self, value, *args):
		return self.model.objects.get_or_create(name = value, ename= args[1], continent=args[2])[0]

	
class Placeresources(resources.ModelResource):
	def get_instance(self, instance_loader, row):
		return False
	city = fields.Field(column_name='city', attribute='city', widget=CityWidget(City, 'name'))
	country = Myfield(column_name='country', attribute='country', widget=CountryWidget(Country, 'name'))

	class Meta:		
		model = Airport
		fields = ('id','name','ename','country','city','oon','iata','ngrad', 'nmin', 'wgrad', 'wmin', 'typetime')
		export_order = fields
		skip_unchanged = True
        report_skipped = False







class AirportAdmin(ImportExportActionModelAdmin,admin.ModelAdmin):
    resource_class = Placeresources
    fieldsets = [
        ('Название', {'fields':['name']}),
		('Английское Название', {'fields':['ename']}),
        ('Город', {'fields':['city']}),
        ('Страна', {'fields':['country']}),
        ('iata', {'fields':['iata']}),
        ('oon', {'fields':['oon']}),
        ('ngrad', {'fields':['ngrad']}),
        ('nmin', {'fields':['nmin']}),
        ('wgrad', {'fields':['wgrad']}),
        ('wmin', {'fields':['wmin']}),
        ('typetime', {'fields':['typetime']}),
		('slug', {'fields':['slug']}),
    ]
admin.site.register(Airport, AirportAdmin)
admin.site.register(Country)
admin.site.register(City)
