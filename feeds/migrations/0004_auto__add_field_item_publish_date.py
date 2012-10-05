# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Item.publish_date'
        db.add_column('feeds_item', 'publish_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 5, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Item.publish_date'
        db.delete_column('feeds_item', 'publish_date')


    models = {
        'feeds.feed': {
            'Meta': {'object_name': 'Feed'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page_url': ('django.db.models.fields.URLField', [], {'max_length': '400'}),
            'parser': ('django.db.models.fields.TextField', [], {'max_length': '400'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '400'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'updated_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'feeds.item': {
            'Meta': {'ordering': "['-publish_date']", 'object_name': 'Item'},
            'enclosure': ('django.db.models.fields.URLField', [], {'max_length': '400'}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': "orm['feeds.Feed']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'updated_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['feeds']