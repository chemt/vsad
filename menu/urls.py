
from django.conf.urls.defaults import *
from django.views.generic import list_detail
from models import MenuCategory, MenuCategoryZakaz


MenuCategory_list_info = {
    'queryset' :   MenuCategory.objects.all(),
	'template_object_name': 'Category',
}

MenuCategoryZakaz_list_info = {
    'queryset' :   MenuCategoryZakaz.objects.all(),
    'template_object_name': 'Category',
}


urlpatterns = patterns('',
    (r'^$', list_detail.object_list, MenuCategory_list_info),
    (r'^/vip/zamovlennya$', list_detail.object_list, MenuCategoryZakaz_list_info),
    (r'^/vip/add/(?P<id>\d+)/(?P<quantity>\d+)', 'menu.views.add_to_cart')
)
