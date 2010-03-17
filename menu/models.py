# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy  as _

class MenuCategory(models.Model):
    name = models.CharField(_(u"Назва Розділу"),max_length=200)
    ordering = models.IntegerField(_(u"Порядок сортування"), blank = True, null = True)

    class Meta:
        ordering = ["ordering", "name"]
        verbose_name = _(u"Розділ меню")
        verbose_name_plural  = _(u"Розділи меню")
        
    class Admin(admin.ModelAdmin):
        fieldsets = (
            (None,		{'fields': ('name',)}),
          #  (_(u"Сортування"),		{'fields': ('ordering',)}),
            )
        list_display = ('name', 'ordering',)
        search_fields  = ('name',)

    def __unicode__(self):
        return u"%s" % self.name


class MenuItem(models.Model):
    name     = models.CharField(_(u"Назва пункту меню"), max_length=200)
    ordering = models.IntegerField(_(u"Порядок сортування"), blank = True, null = True)
    category = models.ForeignKey(MenuCategory, verbose_name=_(u"Розділ"))
    amount   = models.CharField(_(u"Порція"), max_length=200, blank=True, null = True)
    price    = models.CharField(_(u"Ціна"), max_length=200, blank=True, null = True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["ordering", "name", "amount", "price"]
        verbose_name = _(u"Пункт меню")
        verbose_name_plural  = _(u"Пункти меню")

    class Admin(admin.ModelAdmin):
        fieldsets = (
            (None,		{'fields': ('name', 'category')}),
            (_(u"Страва"),		{'fields': ('amount', 'price')}),
            (_(u"Сортування"),		{'fields': ('ordering',)}),
            )
        list_display = ('name', 'category', 'amount', 'price')
        search_fields  = ('name', "amount", "price")
