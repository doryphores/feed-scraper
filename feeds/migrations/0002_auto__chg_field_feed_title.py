# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Feed.title'
        db.alter_column('feeds_feed', 'title', self.gf('django.db.models.fields.CharField')(max_length=400))

    def backwards(self, orm):

        # Changing field 'Feed.title'
        db.alter_column('feeds_feed', 'title', self.gf('django.db.models.fields.TextField')(max_length=400))

    models = {
        'feeds.feed': {
            'Meta': {'object_name': 'Feed'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page_url': ('django.db.models.fields.URLField', [], {'max_length': '400'}),
            'parser': ('django.db.models.fields.TextField', [], {'max_length': '400'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '400'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        }
    }

    complete_apps = ['feeds']