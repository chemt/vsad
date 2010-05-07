# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.template import RequestContext
from models import GuestBook
from forms import GuestbookForm
from settings import REPORT_EMAILS

def guestbook(request):
    added = False
	
    if request.method == 'POST': # If the form has been submitted...
        form = GuestbookForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            message_text = u'Імя: %s \n Відгук: %s' % (data['name'], data['text'])
            send_mail(u'Новий відгук на сайті', message_text, 'auto@example.com',
                        REPORT_EMAILS, fail_silently=False)
            added = True
            form = GuestbookForm()

    else:
        form = GuestbookForm()

    entries = GuestBook.objects.all().order_by("-date")
    templates = {'form': form, 'entries': entries, 'added':added }
    c = RequestContext(request, templates)
    return render_to_response("guestbook.html", c)
