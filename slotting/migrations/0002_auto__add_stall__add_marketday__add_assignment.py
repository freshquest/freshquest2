# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Stall'
        db.create_table(u'slotting_stall', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('building', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('stall_number', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal(u'slotting', ['Stall'])

        # Adding model 'MarketDay'
        db.create_table(u'slotting_marketday', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('market_day_id', self.gf('uuidfield.fields.UUIDField')(unique=True, max_length=32, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'slotting', ['MarketDay'])

        # Adding model 'Assignment'
        db.create_table(u'slotting_assignment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('market_day', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['slotting.MarketDay'])),
            ('stall', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['slotting.Stall'])),
            ('vendor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['slotting.Vendor'])),
        ))
        db.send_create_signal(u'slotting', ['Assignment'])


    def backwards(self, orm):
        # Deleting model 'Stall'
        db.delete_table(u'slotting_stall')

        # Deleting model 'MarketDay'
        db.delete_table(u'slotting_marketday')

        # Deleting model 'Assignment'
        db.delete_table(u'slotting_assignment')


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