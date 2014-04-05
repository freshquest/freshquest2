# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'VendorProfile'
        db.create_table(u'profiles_vendorprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('vendor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['slotting.Vendor'])),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('accepts_preorders', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'profiles', ['VendorProfile'])

        # Adding M2M table for field categories on 'VendorProfile'
        m2m_table_name = db.shorten_name(u'profiles_vendorprofile_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('vendorprofile', models.ForeignKey(orm[u'profiles.vendorprofile'], null=False)),
            ('category', models.ForeignKey(orm[u'profiles.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['vendorprofile_id', 'category_id'])

        # Adding model 'Category'
        db.create_table(u'profiles_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category_id', self.gf('uuidfield.fields.UUIDField')(unique=True, max_length=32, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'profiles', ['Category'])


    def backwards(self, orm):
        # Deleting model 'VendorProfile'
        db.delete_table(u'profiles_vendorprofile')

        # Removing M2M table for field categories on 'VendorProfile'
        db.delete_table(db.shorten_name(u'profiles_vendorprofile_categories'))

        # Deleting model 'Category'
        db.delete_table(u'profiles_category')


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
            'vendor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['slotting.Vendor']"}),
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