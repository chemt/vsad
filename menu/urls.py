
from django.conf.urls.defaults import *
from django.views.generic import list_detail
from models import MenuCategory


MenuCategory_list_info = {
    'queryset' :   MenuCategory.objects.all(),
	'template_object_name': 'Category',
}

urlpatterns = patterns('',
    (r'^$', list_detail.object_list, MenuCategory_list_info),
)