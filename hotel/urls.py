
from django.conf.urls.defaults import *
from django.views.generic import list_detail
from models import Nomer


Nomer_list_info = {
    'queryset' :   Nomer.objects.all(),
    'template_object_name': 'Nomer',
}

urlpatterns = patterns('',
    (r'^$', list_detail.object_list, Nomer_list_info),
)
