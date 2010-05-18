from cart import Cart
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
#
#from menu.models import MenuItem
#
#
#def rest_add_to_cart(request, id, quantity):
#    product = MenuItem.objects.get(id=id)
#    cart = Cart(request)
#    cart.add(product, product.unit_price, quantity)
#
##def remove_from_cart(request, product_id):
##    product = Product.objects.get(id=product_id)
##    cart = Cart(request)
##    cart.remove(product)
#

def get_cart(request):
    return HttpResponseRedirect(request.META['HTTP_REFERER']) 
    #return render_to_response('cart/view_cart.html', RequestContext(request,dict(cart=Cart(request))))

def clear_cart(request):
    cart=Cart(request)
    cart.clear()
    return get_cart(request)

def inc_cart_item(request, id):
    cart=Cart(request)
    cart.inc(id)
    return get_cart(request)

def dec_cart_item(request, id):
    cart=Cart(request)
    cart.dec(id)
    return get_cart(request)

def del_cart_item(request, id):
    cart=Cart(request)
    cart.delete(id)
    return get_cart(request)
