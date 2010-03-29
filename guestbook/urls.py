
from django.conf.urls.defaults import *
from views import guestbook



urlpatterns = patterns('',
    (r'^$', guestbook)
)