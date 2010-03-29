# -*- coding: utf-8 -*-

from django.contrib import admin
from models import Zayavka

admin.site.register(Zayavka, Zayavka.Admin)

