# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy  as _
from hotel.models import Nomer



class Zayavka(models.Model):
    vip_card = models.CharField(_(u"Номер VIP картки"), max_length=200, blank=False)
    name = models.CharField(_(u"Ім’я"), max_length=200, blank=False)
    contact = models.CharField(_(u"Контактний телефон"), max_length=200, blank=False)
    
    date = models.CharField(_(u"На коли"), max_length=200, blank=True)
    
    restoran = models.BooleanField(_(u"Замовити страву з ресторану"), default=False)
    pizza = models.BooleanField(_(u"Замовити піцу"), default=False)
    hotel = models.BooleanField(_(u"Замовити номер в готелі"), default=False)
    sauna = models.BooleanField(_(u"Замовити сауну"), default=False)
    
    text = models.TextField(_(u"Текст заявки"), max_length=1000, blank=True)
    
    class Meta:
        ordering = ["date", "name"]
        verbose_name = _(u"Замовлення")
        verbose_name_plural = _(u"Замовлення")
        
    class Admin(admin.ModelAdmin):
        fieldsets = (
            (None, 		{'fields': ("vip_card", "name", "contact", "date")}),
            (_(u"Тип замовлення"), 	{'fields': ("restoran", "pizza", "hotel", "sauna")}),
            (_(u"Текст замовлення"), 	{'fields': ("text",)}),
            )
        list_display = ("date", "name", "contact", "restoran", "pizza", "hotel", "sauna")
        search_fields = ("date", "name", "text", "vip_card")

    def __unicode__(self):
        return u"%s" % self.name

class ZayavkaHotel(models.Model):
    name = models.CharField(_(u"Ім’я"), max_length=200, blank=False)
    contact = models.CharField(_(u"Контактний телефон"), max_length=200, blank=False)
    date = models.CharField(_(u"На коли"), max_length=200, blank=True)
    text = models.TextField(_(u"Текст заявки"), max_length=1000, blank=True)

    class Meta:
        ordering = ["date", "name"]
        verbose_name = _(u"Замовлення Готелю")
        verbose_name_plural = _(u"Замовлення Готелю")

    class Admin(admin.ModelAdmin):
        fieldsets = (
            (None,         {'fields': ("vip_card", "name", "contact", "date")}),
            (_(u"Текст заявки￿"),     {'fields': ("text",)}),
            )
        list_display = ("date", "name", "contact")
        search_fields = ("date", "name", "text", "contact")

    def __unicode__(self):
        return u"%s" % self.name