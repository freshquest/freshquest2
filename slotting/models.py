from django.db import models
import uuidfield

VENDOR_TYPE = ['farmer', 'dealer', 'commercial', 'prepared_food']

class Vendor(models.Model):
    vendor_id = uuidfield.UUIDField(auto=True, unique=True, editable=False)
    name = models.CharField(max_length=255, help_text='Vendor name')
    vendor_type = models.CharField(max_length=8, choices=map(lambda x: (x, x), VENDOR_TYPE))

    def __unicode__(self):
        return self.name
