# -*- coding: utf-8 -*-

from south.db import db
from django.db import models
from vsad.guestbook.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Changing field 'GuestBook.text'
        # (to signature: django.db.models.fields.TextField(max_length=200))
        db.alter_column('guestbook_guestbook', 'text', orm['guestbook.guestbook:text'])
        
    
    
    def backwards(self, orm):
        
        # Changing field 'GuestBook.text'
        # (to signature: django.db.models.fields.CharField(max_length=200))
        db.alter_column('guestbook_guestbook', 'text', orm['guestbook.guestbook:text'])
        
    
    
    models = {
        'guestbook.guestbook': {
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'text': ('django.db.models.fields.TextField', [], {'max_length': '200'})
        }
    }
    
    complete_apps = ['guestbook']
