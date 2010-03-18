# -*- coding: utf-8 -*-

from django.contrib import admin
from models import PizzaAdd, Pizza
from django.utils.translation import ugettext as _

admin.site.register(PizzaAdd, PizzaAdd.Admin)
admin.site.register(Pizza, Pizza.Admin)

