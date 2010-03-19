# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import User, UserManager
from django.db import models
from django.utils.translation import ugettext_lazy  as _

class VipUser(User):
    # This is the only required field
    card = models.CharField(_(u"Номер VIP картки"), max_length=100, blank=True)
    telephone = models.CharField(_(u"Телефон"), max_length=100, blank=True)
    adress = models.CharField(_(u"Адресса"), max_length=100, blank=True)
    # Use UserManager to get the create_user method, etc.
    objects = UserManager()
    

