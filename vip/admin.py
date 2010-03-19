from django.contrib import admin

from models import *

class VipUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'card', 'telephone')
    fieldsets = (
        (None,		{'fields': ('username', 'email', )}),
        ("VIP",		{'fields': ('first_name', 'last_name', 'card', 'telephone', 'adress')}),
    )
admin.site.register(VipUser, VipUserAdmin)