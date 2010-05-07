
from django.conf.urls.defaults import *
from views import zayavka



urlpatterns = patterns('',
    (r'^$', zayavka)
)
