from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

admin.site.root_path = "/admin/" # there is probably a bug in django...


urlpatterns = patterns('django.views.generic.simple',
    (r'^$',             'direct_to_template', {'template': 'index.htm'}),
    (r'^index.htm$',    'direct_to_template', {'template': 'index.htm'}),
    (r'^book.htm$',     'direct_to_template', {'template': 'book.htm'}),
    (r'^contact.htm$',  'direct_to_template', {'template': 'contact.htm'}),
    (r'^hotel.htm$',    'direct_to_template', {'template': 'hotel.htm'}),
    (r'^pitseriya.htm$','direct_to_template', {'template': 'pitseriya.htm'}),
    (r'^restaurant.htm$', 'direct_to_template', {'template': 'restaurant.htm'}),
    (r'^sauna.htm$',    'direct_to_template', {'template': 'sauna.htm'}),
    
    (r'^menu.htm', include('vsad.menu.urls')),
    (r'^pizza.htm', include('vsad.pizza.urls')),
)

urlpatterns += patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),
    
)

if settings.DEBUG:
    urlpatterns+= patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
    )

