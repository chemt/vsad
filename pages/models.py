# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail.fields import ImageWithThumbnailsField
from markitup.fields import MarkupField

class Page(models.Model):
    name = models.CharField(_(u"Заголовок"), max_length=250)
    slug = models.SlugField(_(u"адреса URL"), max_length=250)
    image = ImageWithThumbnailsField(_(u"Картинка"), blank=True, upload_to='page_images', thumbnail={'size': (750, 750)})
    text = MarkupField(_(u" Текст"), blank=True) 
    class Meta:
        ordering = ["slug", "name"]
        verbose_name = _(u"Сторінка")
        verbose_name_plural = _(u"Сторінки")

