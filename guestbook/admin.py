# -*- coding: utf-8 -*-

from django.contrib import admin
from models import GuestBook

admin.site.register(GuestBook, GuestBook.Admin)

