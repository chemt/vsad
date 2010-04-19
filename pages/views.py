from django.template import loader, RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from models import Page
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.safestring import mark_safe
from django.core.xheaders import populate_xheaders


def page(request, slug):
    f = get_object_or_404(Page, slug__exact=slug)

    f.name = mark_safe(f.name)
    f.text = mark_safe(f.text)

    c = RequestContext(request, {
        'page': f,
    })
    response = render_to_response('page.html',c)
    populate_xheaders(request, response, Page, f.id)
    return response