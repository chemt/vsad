# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy  as _
from sorl.thumbnail.fields import ImageWithThumbnailsField 

class Pizza(models.Model):
    name = models.CharField(_(u"Назва піци"),max_length=200)
    ordering = models.IntegerField(_(u"Порядок сортування"), blank=True, null=True)
    
    sklad = models.CharField(_(u"Склад"), max_length=200, blank=True)

    big_amaunt = models.CharField(_(u"Маса (велика)"), max_length=200, blank=True)
    big_price = models.CharField(_(u"Ціна (велика)"), max_length=200,blank=True)
    small_amaunt = models.CharField(_(u"Маса (мала)"), max_length=200,blank=True)
    small_price = models.CharField(_(u"Ціна (мала)"), max_length=200,blank=True)

    image    = ImageWithThumbnailsField(_(u"Фото"),  blank=True, upload_to='profiles',
                                     thumbnail={'size': (80, 80)})


    class Meta:
        ordering = ["ordering", "name"]
        verbose_name = _(u"Піца")
        verbose_name_plural  = _(u"Піци")
        
    class Admin(admin.ModelAdmin):
        fieldsets = (
            (None,		{'fields': ('name', 'sklad', 'image')}),
            (_(u"Велика"),		{'fields': ('big_amaunt','big_price',)}),
            (_(u"Мала"),		{'fields': ('small_amaunt','small_price',)}),
            (_(u"Сортування"),		{'fields': ('ordering',)}),
            )
        list_display = ('name', 'ordering','big_amaunt','big_price', 'small_amaunt','small_price', )
        search_fields  = ('name',)

    def __unicode__(self):
        return u"%s" % self.name


class PizzaAdd(models.Model):
    name = models.CharField(_(u"Назва додатку"),max_length=200)
    ordering = models.IntegerField(_(u"Порядок сортування"), blank=True, null=True)
    
    amaunt = models.CharField(_(u"Порція"), max_length=200, blank=True)
    price = models.CharField(_(u"Ціна"), max_length=200,blank=True)

    image    = ImageWithThumbnailsField(_(u"Фото"),  blank=True, upload_to='profiles',
                                     thumbnail={'size': (80, 80)})


    class Meta:
        ordering = ["ordering", "name"]
        verbose_name = _(u"Додаток до піци")
        verbose_name_plural  = _(u"Додатки до піци")
        
    class Admin(admin.ModelAdmin):
        fieldsets = (
            (None,		
            	{'fields': ('name', 'ordering', 'image', 'amaunt', 'price',)}),
            )
        list_display = ('name', 'ordering', 'amaunt','price',)
        search_fields  = ('name',)

    def __unicode__(self):
        return u"%s" % self.name
