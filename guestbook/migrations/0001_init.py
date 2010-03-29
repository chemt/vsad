# -*- coding: utf-8 -*-

from south.db import db
from django.db import models
from vsad.guestbook.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'GuestBook'
        db.create_table('guestbook_guestbook', (
            ('id', orm['guestbook.GuestBook:id']),
            ('name', orm['guestbook.GuestBook:name']),
            ('text', orm['guestbook.GuestBook:text']),
            ('date', orm['guestbook.GuestBook:date']),
        ))
        db.send_create_signal('guestbook', ['GuestBook'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'GuestBook'
        db.delete_table('guestbook_guestbook')
        
    
    
    models = {
        'guestbook.guestbook': {
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }
    
    complete_apps = ['guestbook']
