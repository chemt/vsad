# -*- coding: utf-8 -*-

from cart import Cart
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from settings import REPORT_EMAILS
from django.template import loader

from forms import VIPForm

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

def checkout(request):
    if request.method == 'POST': # If the form has been submitted...
        form = VIPForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            cart = Cart(request) 
            message_text = render_to_string('cart/email.txt', { 'form': form.cleaned_data, 'cart':cart })
            send_mail(  u'Нове замовлення. VIP %s' % form.cleaned_data['vip'],
                        message_text, 'auto@vyshnevysad.com.ua',
                        REPORT_EMAILS, 
                        fail_silently=False)
            
            cart.checkout()
            return render_to_response('cart/view_cart.html', RequestContext(request,dict(cart=cart)))
    else:
        form = VIPForm() # An unbound form
    
    return render_to_response('cart/vip_form.html', RequestContext(request,dict(form=form)))