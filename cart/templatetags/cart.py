# -*- coding: utf-8 -*-
from django import template
from django.template.loader import get_template
from django.template import Context

register = template.Library()


from vsad.cart import Cart


@register.simple_tag
def show_cart(request):
    cart = Cart(request)
    t = get_template('cart/cart.html')
    html = t.render(Context({'cart': cart}))
    return html

