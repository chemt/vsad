# -*- coding: utf-8 -*-

from django.contrib import admin
from menu.models import MenuItem, MenuCategory


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
            (None, 		{'fields': ('name', 'image', 'ordering', 'category',
            						'col1', 'col2', 'col3', 'col4',)}),
            )
    ordering = ["ordering", 'image', "name", ]
    extra = 15

admin.site.register(MenuItem, MenuItem.Admin)

admin.site.register(MenuCategory,
    inlines=[ItemInline],
    form=MenuForm,
)

from menu.models import  MenuCategoryZakaz
admin.site.register(MenuCategoryZakaz, MenuCategoryZakaz.Admin)
