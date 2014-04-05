# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Stall.section'
        db.add_column(u'slotting_stall', 'section',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=8),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Stall.section'
        db.delete_column(u'slotting_stall', 'section')


    models = {
        u'slotting.assignment': {
            'Meta': {'object_name': 'Assignment'},
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
            'Meta': {'object_name': 'Stall'},
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