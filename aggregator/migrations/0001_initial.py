# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Blog'
        db.create_table('aggregator_blog', (
            ('added_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feed_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.CharField')(default='Sin Nombre', max_length=200)),
        ))
        db.send_create_signal('aggregator', ['Blog'])

        # Adding model 'Post'
        db.create_table('aggregator_post', (
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('title', self.gf('django.db.models.fields.CharField')(default='Sin Titulo', max_length=200)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('blog', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['aggregator.Blog'])),
            ('link', self.gf('django.db.models.fields.URLField')(unique=True, max_length=200)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('aggregator', ['Post'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Blog'
        db.delete_table('aggregator_blog')

        # Deleting model 'Post'
        db.delete_table('aggregator_post')
    
    
    models = {
        'aggregator.blog': {
            'Meta': {'object_name': 'Blog'},
            'added_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'feed_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Sin Nombre'", 'max_length': '200'})
        },
        'aggregator.post': {
            'Meta': {'object_name': 'Post'},
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['aggregator.Blog']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Sin Titulo'", 'max_length': '200'})
        }
    }
    
    complete_apps = ['aggregator']
