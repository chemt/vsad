
from django.conf.urls.defaults import *
from django.views.generic import list_detail
from models import MenuCategory


Entry_list_info = {
    'queryset' :   MenuCategory.objects.all(),
	'template_object_name': 'Category',
}

urlpatterns = patterns('',
    (r'^$', list_detail.object_list, Entry_list_info),
    #(r'^(?P<object_id>\d+)/$', list_detail.object_detail, Entry_list_info),
)