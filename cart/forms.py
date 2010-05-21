# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy  as _
from math_captcha.forms import MathCaptchaForm
from django import forms

class VIPForm(MathCaptchaForm):
    vip = forms.IntegerField(label=_(u"Номер VIP карти"), required=True)
    phone = forms.CharField(label=_(u"Контактный номер телефону"), required=True, max_length=50)
    name = forms.CharField(label=_(u"Ім’я"))
    message = forms.CharField(label=_(u"Додаткове повідомлення"), widget=forms.widgets.Textarea(), required=False)

