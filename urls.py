from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.auth.views import login, logout

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

    (r'^vip_', include('vip.urls')),
)

urlpatterns += patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),
    (r'^accounts/login/$',  login),
    (r'^accounts/logout/$', logout),

)



from django.views.generic.simple import direct_to_template
from django.contrib.auth import views as auth_views

from registration.views import activate
from registration.views import register


urlpatterns += patterns('',
                       # Activation keys get matched by \w+ instead of the more specific
                       # [a-fA-F0-9]{40} because a bad activation key should still get to the view;
                       # that way it can return a sensible "invalid key" message instead of a
                       # confusing 404.
                       url(r'^activate_(?P<activation_key>\w+)/$',
                           activate,
                           name='registration_activate'),
                       url(r'^login$',
                           auth_views.login,
                           {'template_name': 'registration/login.html'},
                           name='auth_login'),
                       url(r'^logout$',
                           auth_views.logout,
                           {'template_name': 'registration/logout.html'},
                           name='auth_logout'),
                       url(r'^password/change/$',
                           auth_views.password_change,
                           name='auth_password_change'),
                       url(r'^password/change/done/$',
                           auth_views.password_change_done,
                           name='auth_password_change_done'),
                       url(r'^password/reset/$',
                           auth_views.password_reset,
                           name='auth_password_reset'),
                       url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
                           auth_views.password_reset_confirm,
                           name='auth_password_reset_confirm'),
                       url(r'^password/reset/complete/$',
                           auth_views.password_reset_complete,
                           name='auth_password_reset_complete'),
                       url(r'^password/reset/done/$',
                           auth_views.password_reset_done,
                           name='auth_password_reset_done'),
                       url(r'^register$',
                           register,
                           name='registration_register', form_class=""),
                       url(r'^register_complete_$',
                           direct_to_template,
                           {'template': 'registration/registration_complete.html'},
                           name='registration_complete'),
                       )

if settings.DEBUG:
    urlpatterns+= patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
    )

