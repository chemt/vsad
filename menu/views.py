# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from cart import Cart
from menu.models import MenuItem

def add_to_cart(request, id, quantity):
    product = MenuItem.objects.get(id=id)
    cart = Cart(request)
    cart.add(product, product.price(), quantity)
    return HttpResponseRedirect(u"/menu.htm/vip/zamovlennya")
