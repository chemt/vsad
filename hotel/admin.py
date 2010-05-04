# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext as _

from hotel.models import Nomer, NomerPhoto

from django import forms


class NomerForm(forms.ModelForm):
    model = Nomer

class PhotoInline(admin.TabularInline):
#class PhotoInline(admin.StackedInline):
    model = NomerPhoto
    fieldsets = (
            (None,        {'fields': ('name', 'photo')}),
            )
    ordering = ["name", ]
    extra = 5

admin.site.register(Nomer,
    inlines = [PhotoInline],
    form = NomerForm,
)
