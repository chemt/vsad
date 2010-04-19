# -*- coding: utf-8 -*-

from django.contrib import admin
from models import Page
from django.utils.translation import ugettext as _
from markitup.widgets import AdminMarkItUpWidget

class PageAdmin(admin.ModelAdmin):
#    formfield_overrides = {models.TextField: {'widget': AdminMarkItUpWidget}}
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = (
            (_(u"Сторінка"),        {'fields': ('name', 'slug', 'image')}),
            (_(u"Текст сторінки"),        {'fields': ('text', )}),
            )
    list_display = ('name', 'slug')
    search_fields  = ('name', 'text', 'slug')
    
admin.site.register(Page, PageAdmin)
