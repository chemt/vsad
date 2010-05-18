# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'MenuCategoryZakaz'
        db.create_table('menu_menucategoryzakaz', (
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['menu.MenuCategory'], unique=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('menu', ['MenuCategoryZakaz'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'MenuCategoryZakaz'
        db.delete_table('menu_menucategoryzakaz')
    
    
    models = {
        'menu.menucategory': {
            'Meta': {'object_name': 'MenuCategory'},
            'col1': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'col2': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'col3': ('django.db.models.fields.CharField', [], {'default': "u'\\u041f\\u043e\\u0440\\u0446\\u0456\\u044f'", 'max_length': '200', 'blank': 'True'}),
            'col4': ('django.db.models.fields.CharField', [], {'default': "u'\\u0426\\u0456\\u043d\\u0430'", 'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'menu.menucategoryzakaz': {
            'Meta': {'object_name': 'MenuCategoryZakaz'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['menu.MenuCategory']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'menu.menuitem': {
            'Meta': {'object_name': 'MenuItem'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['menu.MenuCategory']"}),
            'col1': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'col2': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'col3': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'col4': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }
    
    complete_apps = ['menu']
