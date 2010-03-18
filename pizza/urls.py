
from django.conf.urls.defaults import *
from django.views.generic import list_detail
from models import Pizza, PizzaAdd


Pizza_list_info = {
    'queryset' :   Pizza.objects.all(),
	'template_object_name': 'Pizza',

	'extra_context': {
		'pizzaadd_list': PizzaAdd.objects.all(),
	},
}

urlpatterns = patterns('',
    (r'^$', list_detail.object_list, Pizza_list_info),
    #(r'^(?P<object_id>\d+)/$', list_detail.object_detail, Entry_list_info),
)