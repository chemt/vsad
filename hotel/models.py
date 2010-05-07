# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy  as _
from sorl.thumbnail.fields import ImageWithThumbnailsField
from markitup.fields import MarkupField 

class Nomer(models.Model):
    name = models.CharField(_(u"Заголовок"), max_length=200, blank=True)
    text = MarkupField(_(u"Опис номеру"), blank=True)
    
    def __unicode__(self):
        return u"%s" % self.name
    
    class Meta():
        verbose_name = _(u"Номер")
        verbose_name_plural = _(u"Номери")
        
    class Admin():
        fieldsets = (
            (None, {'fields': ('name', 'text')}),
           )

class NomerPhoto(models.Model):
    photo = ImageWithThumbnailsField(_(u"Картинка"), blank=True, upload_to='hotel_images', thumbnail={'size': (200, 150)})
    nomer = models.ForeignKey(Nomer, verbose_name=_(u"Номер"))
    name = models.CharField(_("Підпис"), max_length=200, blank=True)

    def __unicode__(self):
        return u"%s" % self.name
    
    class Meta():
        verbose_name = _(u"Фото номеру")
        verbose_name_plural = _(u"Фото номерів")


