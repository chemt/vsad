# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'cart.views.get_cart', name="get_cart"),
    url(r'^/clear$', 'cart.views.clear_cart', name="clear_cart"),
    url(r'^/inc_(?P<id>\d+)$', 'cart.views.inc_cart_item', name="inc_cart_item"),
    url(r'^/dec_(?P<id>\d+)$', 'cart.views.dec_cart_item', name="dec_cart_item"),
    url(r'^/del_(?P<id>\d+)$', 'cart.views.del_cart_item', name="del_cart_item"),
) 
