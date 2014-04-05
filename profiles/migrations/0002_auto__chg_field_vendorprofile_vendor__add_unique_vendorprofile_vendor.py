# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'VendorProfile.vendor'
        db.alter_column(u'profiles_vendorprofile', 'vendor_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['slotting.Vendor'], unique=True))
        # Adding unique constraint on 'VendorProfile', fields ['vendor']
        db.create_unique(u'profiles_vendorprofile', ['vendor_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'VendorProfile', fields ['vendor']
        db.delete_unique(u'profiles_vendorprofile', ['vendor_id'])


        # Changing field 'VendorProfile.vendor'
        db.alter_column(u'profiles_vendorprofile', 'vendor_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['slotting.Vendor']))

    models = {
        u'profiles.category': {
            'Meta': {'object_name': 'Category'},
            'category_id': ('uuidfield.fields.UUIDField', [], {'unique': 'True', 'max_length': '32', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'profiles.vendorprofile': {
            'Meta': {'object_name': 'VendorProfile'},
            'accepts_preorders': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['profiles.Category']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'vendor': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['slotting.Vendor']", 'unique': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'slotting.vendor': {
            'Meta': {'object_name': 'Vendor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'vendor_id': ('uuidfield.fields.UUIDField', [], {'unique': 'True', 'max_length': '32', 'blank': 'True'}),
            'vendor_type': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        }
    }

    complete_apps = ['profiles']