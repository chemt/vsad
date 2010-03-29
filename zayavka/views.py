# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.template import RequestContext
from models import Zayavka
from forms import ZayavkaForm
from settings import REPORT_EMAILS

def zayavka(request):
    if request.method == 'GET':
        form=ZayavkaForm(request.GET)
    elif request.method == 'POST': # If the form has been submitted...
        form=ZayavkaForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            
            message_text = render_to_string('mail_zamovlenya.txt', { 'data': data })
            send_mail(u'Нова заявка на сайті', message_text, 'auto@example.com',
                        REPORT_EMAILS, fail_silently=False)
            added = True
            form=ZayavkaForm()
            return render_to_response("zayavka_ok.htm", RequestContext(request))

    else:
        form=ZayavkaForm()

    templates = {'form': form, }
    c = RequestContext(request, templates)
    return render_to_response("zayavka.htm", c)