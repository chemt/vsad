# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy  as _
from sorl.thumbnail.fields import ImageWithThumbnailsField 

class MenuCategory(models.Model):
    name = models.CharField(_(u"Назва Розділу"), max_length=200)
    ordering = models.IntegerField(_(u"Порядок сортування"), blank=True, null=True)
    
    col1 = models.CharField(_(u"Назва першої колонки"), max_length=200, blank=True)

    col2 = models.CharField(_(u"Назва другої колонки"), max_length=200, blank=True)

    col3 = models.CharField(_(u"Назва третьої колонки"), max_length=200, blank=True,
                            default=_(u"Порція"))

    col4 = models.CharField(_(u"Назва четвертої колонки"), max_length=200, blank=True,
                            default=_(u"Ціна"))


    class Meta:
        ordering = ["ordering", "name"]
        verbose_name = _(u"Розділ меню")
        verbose_name_plural = _(u"Розділи меню")
        
    class Admin(admin.ModelAdmin):
        fieldsets = (
            (None, 		{'fields': ('name',)}),
            (_(u"Сортування"), 		{'fields': ('ordering',)}),
            (_(u"Назви колонок"), 		{'fields': ('col1', 'col2', 'col3', 'col4',)}),
            )
        list_display = ('name', 'ordering', 'col1', 'col2', 'col3', 'col4',)
        search_fields = ('name', 'col1', 'col2', 'col3', 'col4',)

    def __unicode__(self):
        return u"%s" % self.name


class MenuItem(models.Model):
    name = models.CharField(_(u"Назва пункту меню"), max_length=200)
    image = ImageWithThumbnailsField(_(u"Фото"), blank=True, upload_to='profiles',
                                     thumbnail={'size': (80, 80)})
    category = models.ForeignKey(MenuCategory, verbose_name=_(u"Розділ"))
    ordering = models.IntegerField(_(u"Порядок сортування"), blank=True, null=True)
    col1 = models.CharField(_(u"Колонка 1"), max_length=200, blank=True)

    col2 = models.CharField(_(u"Колонка 2"), max_length=200, blank=True)

    col3 = models.CharField(_(u"Колонка 3"), max_length=200, blank=True)

    col4 = models.CharField(_(u"Колонка 4"), max_length=200, blank=True)


    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['ordering', 'image', 'name', 'col1', 'col2', 'col3', 'col4', ]
        verbose_name = _(u"Пункт меню")
        verbose_name_plural = _(u"Пункти меню")

    class Admin(admin.ModelAdmin):
        fieldsets = (
            (None, 		{'fields': ('name', 'category')}),
            (_(u"Страва"), 		{'fields': ('image', 'col1', 'col2', 'col3', 'col4',)}),
            (_(u"Сортування"), 		{'fields': ('ordering',)}),
            )
        list_display = ('name', 'category', 'col1', 'col2', 'col3', 'col4',)
        list_filter = ('category',)
        search_fields = ('name', 'col1', 'col2', 'col3', 'col4',)
