# -*- coding: utf-8 -*-

from south.db import db
from django.db import models
from vsad.zayavka.models import *

class Migration:
    
    def forwards(self, orm):
        "Write your forwards migration here"
    
    
    def backwards(self, orm):
        "Write your backwards migration here"
    
    
    models = {
        'zayavka.zayavka': {
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'hotel': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pizza': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'restoran': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'sauna': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '200', 'blank': 'True'}),
            'vip_card': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }
    
    complete_apps = ['zayavka']
