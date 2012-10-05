# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Feed'
        db.create_table('feeds_feed', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')(max_length=400)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=400)),
            ('page_url', self.gf('django.db.models.fields.URLField')(max_length=400)),
            ('parser', self.gf('django.db.models.fields.TextField')(max_length=400)),
        ))
        db.send_create_signal('feeds', ['Feed'])


    def backwards(self, orm):
        # Deleting model 'Feed'
        db.delete_table('feeds_feed')


    models = {
        'feeds.feed': {
            'Meta': {'object_name': 'Feed'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page_url': ('django.db.models.fields.URLField', [], {'max_length': '400'}),
            'parser': ('django.db.models.fields.TextField', [], {'max_length': '400'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '400'}),
            'title': ('django.db.models.fields.TextField', [], {'max_length': '400'})
        }
    }

    complete_apps = ['feeds']