from django.shortcuts import render
from django.conf import settings
from django.views.generic import ListView, TemplateView
from .models import City, Country, Airport

PAGINATE_PRODUCTS_BY = getattr(settings, 'PAGINATE_PRODUCTS_BY', 20)

PLACE = dict(airport=Airport,
                city=City,
                country=Country
                
)
class PlaceList(ListView):
	template_name = ''
	paginate_by = PAGINATE_PRODUCTS_BY
	context_object_name = 'place_list'

	def dispatch(self, request, *args, **kwargs):
		#self.place_class = PLACE[kwargs.get('place')]
		self.template_name = 'place/%s_list.html'% (kwargs.get('place'))
		return super(PlaceList, self).dispatch(request, *args, **kwargs)

	def get_queryset(self):
		return Airport.objects.all()


class PlaceDetail(TemplateView):

	
	
	#context_object_name = 'place'
	pk_url_kwarg = 'pk'
	place = 'place'
	template_name = ''
	def get_context_data(self, **kwargs):
		self.place_funck = self.PLACE[kwargs.get('place')]
		self.template_name = 'place/%s_detail.html'% (kwargs.get('place'))
		context = super(PlaceDetail, self).get_context_data(**kwargs)
		context['place'] = self.place_funck(self, **kwargs)
		return context
	
	def airport(self, **kwargs):
		pk = self.kwargs.get(self.pk_url_kwarg)
		ctx = Airport.objects.get(pk=pk)
		return ctx
	def city(self, **kwargs):
		pk = self.kwargs.get(self.pk_url_kwarg)
		ctx = Airport.objects.get(city_id=pk)
		return ctx
	def country(self, **kwargs):
		pk = self.kwargs.get(self.pk_url_kwarg)
		ctx = Airport.objects.get(country_id=pk)
		return ctx

	PLACE = dict(airport=airport,
                city=city,
                country=country
                
	)


