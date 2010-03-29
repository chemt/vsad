# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy  as _

class GuestBook(models.Model):
    name = models.CharField(_(u"Ім’я"),max_length=200)
    text = models.TextField(_(u"Відгук"), max_length=200, blank=False)
    date = models.DateField(_(u"Дата"), auto_now_add=True)

    class Meta:
        ordering = ["date", "name"]
        verbose_name = _(u"Гостьова книга")
        verbose_name_plural  = _(u"Гостьова книга")
        
    class Admin(admin.ModelAdmin):
        fieldsets = (
            (None,		{'fields': ("name", "text")}),
            )
        list_display = ("date", "name" )
        search_fields  = ("date", "name", "text")

    def __unicode__(self):
        return u"%s" % self.name
