# -*- coding: utf-8 -*-

from south.db import db
from django.db import models
from vsad.zayavka.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Zayavka'
        db.create_table('zayavka_zayavka', (
            ('id', orm['zayavka.Zayavka:id']),
            ('vip_card', orm['zayavka.Zayavka:vip_card']),
            ('name', orm['zayavka.Zayavka:name']),
            ('contact', orm['zayavka.Zayavka:contact']),
            ('date', orm['zayavka.Zayavka:date']),
            ('restoran', orm['zayavka.Zayavka:restoran']),
            ('pizza', orm['zayavka.Zayavka:pizza']),
            ('hotel', orm['zayavka.Zayavka:hotel']),
            ('sauna', orm['zayavka.Zayavka:sauna']),
            ('text', orm['zayavka.Zayavka:text']),
        ))
        db.send_create_signal('zayavka', ['Zayavka'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Zayavka'
        db.delete_table('zayavka_zayavka')
        
    
    
    models = {
        'zayavka.zayavka': {
            'contact': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'date': ('django.db.models.fields.DateField', [], {}),
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
