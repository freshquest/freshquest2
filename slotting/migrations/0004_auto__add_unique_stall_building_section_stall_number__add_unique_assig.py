# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Stall', fields ['building', 'section', 'stall_number']
        db.create_unique(u'slotting_stall', ['building', 'section', 'stall_number'])

        # Adding unique constraint on 'Assignment', fields ['market_day', 'stall', 'vendor']
        db.create_unique(u'slotting_assignment', ['market_day_id', 'stall_id', 'vendor_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Assignment', fields ['market_day', 'stall', 'vendor']
        db.delete_unique(u'slotting_assignment', ['market_day_id', 'stall_id', 'vendor_id'])

        # Removing unique constraint on 'Stall', fields ['building', 'section', 'stall_number']
        db.delete_unique(u'slotting_stall', ['building', 'section', 'stall_number'])


    models = {
        u'slotting.assignment': {
            'Meta': {'unique_together': "(('market_day', 'stall', 'vendor'),)", 'object_name': 'Assignment'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'market_day': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['slotting.MarketDay']"}),
            'stall': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['slotting.Stall']"}),
            'vendor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['slotting.Vendor']"})
        },
        u'slotting.marketday': {
            'Meta': {'object_name': 'MarketDay'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'market_day_id': ('uuidfield.fields.UUIDField', [], {'unique': 'True', 'max_length': '32', 'blank': 'True'})
        },
        u'slotting.stall': {
            'Meta': {'unique_together': "(('building', 'section', 'stall_number'),)", 'object_name': 'Stall'},
            'building': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'section': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'stall_number': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        u'slotting.vendor': {
            'Meta': {'object_name': 'Vendor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'vendor_id': ('uuidfield.fields.UUIDField', [], {'unique': 'True', 'max_length': '32', 'blank': 'True'}),
            'vendor_type': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        }
    }

    complete_apps = ['slotting']