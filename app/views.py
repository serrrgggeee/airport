from django.shortcuts import render
from django.conf import settings
from django.views.generic import ListView, DetailView
from .models import City, Country, Airport

PAGINATE_PRODUCTS_BY = getattr(settings, 'PAGINATE_PRODUCTS_BY', 20)

PLACE = dict(airport=Airport,
                city=City,
                country=Country
                
)
class PlaceList(ListView):
    template_name = 'place/place_list.html'
    paginate_by = PAGINATE_PRODUCTS_BY
    context_object_name = 'place_list'

    def dispatch(self, request, *args, **kwargs):
        self.place_class = PLACE[kwargs.get('place')]
        return super(PlaceList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return self.place_class.objects.all()


class PlaceDetail(DetailView):

	
	template_name = 'place/place_detail.html'
	context_object_name = 'place'
	pk_url_kwarg = 'pk'

	def dispatch(self, request, *args, **kwargs):
		self.place_funck = self.PLACE[kwargs.get('place')]
		return super(PlaceDetail, self).dispatch(request, *args, **kwargs)

	def get_queryset(self):
		return self.place_funck(self, **kwargs)

	def airport(self, **kwargs):
		pk = self.kwargs.get(self.pk_url_kwarg)
		ctx = Airport.objects.get(pk=pk)
		return ctx
	def city(self, **kwargs):
		pk = self.kwargs.get(self.pk_url_kwarg)
		ctx = City.objects.get(pk=pk)
		return ctx
	def country(self, **kwargs):
		pk = self.kwargs.get(self.pk_url_kwarg)
		ctx = Country.objects.get(pk=pk)
		return ctx

	PLACE = dict(airport=airport,
                city=city,
                country=country
                
	)


