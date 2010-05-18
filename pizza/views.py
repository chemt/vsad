# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from cart import Cart
from pizza.models import Pizza

def add_large_to_cart(request, id):
    pizza = Pizza.objects.get(id=id)
    cart = Cart(request)
    price = pizza.big_price.replace(',', '.')
    cart.add(pizza, price, 1)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def add_small_to_cart(request, id):
    pizza = Pizza.objects.get(id=id)
    cart = Cart(request)
    price = pizza.small_price.replace(',', '.')
    cart.add(pizza, price, 1)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
