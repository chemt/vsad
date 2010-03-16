# -*- coding: utf-8 -*-

from django.contrib import admin
from menu.models import MenuItem, MenuCategory
from django.utils.translation import ugettext as _

from django import forms

class MenuForm(forms.ModelForm):
    model = MenuCategory
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.7.2/jquery-ui.min.js',
#            '/static/js/ui.sortable.js',
            '/media/js/menu-sort.js',
        )

class ItemInline(admin.TabularInline):
#class ItemInline(admin.StackedInline):
    model = MenuItem
    fieldsets = (
            (None,		{'fields': ('name', 'category','amount', 'price', 'ordering')}),
            )
    ordering = ["ordering", "name", "amount", "price"]

admin.site.register(MenuCategory,
    inlines = [ItemInline],
    form = MenuForm,
)

#admin.site.register(MenuCategory, MenuCategory.Admin)
admin.site.register(MenuItem, MenuItem.Admin)
