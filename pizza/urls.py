
from django.conf.urls.defaults import *
from django.views.generic import list_detail
from models import Pizza, PizzaAdd


Pizza_list_info = {
    'queryset' :   Pizza.objects.all(),
	'template_object_name': 'Pizza',

	'extra_context': {
		'PizzaAdd_list': PizzaAdd.objects.all(),
	},
}

Pizza_listZakaz_info = {
    'queryset' :   Pizza.objects.all(),
    'template_object_name': 'Pizza',
    'template_name': 'pizza/pizzazakaz_list.html',
}

urlpatterns = patterns('',
    url(r'^$', list_detail.object_list, Pizza_list_info),
    url(r'^/vip/zamovlennya$', list_detail.object_list, Pizza_listZakaz_info),
    url(r'^/vip/add/large/(?P<id>\d+)', 'pizza.views.add_large_to_cart', name="pizza_add_large"),
    url(r'^/vip/add/small/(?P<id>\d+)', 'pizza.views.add_small_to_cart', name="pizza_add_small"),
)
