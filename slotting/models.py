from django.db import models
import uuidfield

VENDOR_TYPE = ['farmer', 'dealer', 'commercial', 'prepared_food']
BUILDINGS = ['a_shed', 'b_line', 'c_shed', 'd_shed', 'e_shed', 'f_shed']
SECTION = ['main', 'center']

class Vendor(models.Model):
    vendor_id = uuidfield.UUIDField(auto=True, unique=True, editable=False)
    name = models.CharField(max_length=255, help_text='Vendor name')
    vendor_type = models.CharField(max_length=8, choices=map(lambda x: (x, x), VENDOR_TYPE))

    def __unicode__(self):
        return self.name

class MarketDay(models.Model):
    market_day_id = uuidfield.UUIDField(auto=True, unique=True, editable=False)
    date = models.DateField()

class Stall(models.Model):
    stall_id = uuidfield.UUIDField(auto=True, unique=True, editable=False)
    building = models.CharField(max_length=8, choices=map(lambda x: (x, x), BUILDINGS))
    section = models.CharField(max_length=8, choices=map(lambda x: (x, x), SECTION))
    stall_number = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('building', 'section', 'stall_number')

    def __unicode__(self):
        return self.building + ' ' + self.section + ' ' + unicode(self.stall_number)

class Assignment(models.Model):
    assignment_id = uuidfield.UUIDField(auto=True, unique=True, editable=False)
    market_day = models.ForeignKey('slotting.MarketDay')
    stall = models.ForeignKey('slotting.Stall')
    vendor = models.ForeignKey('slotting.Vendor')

    class Meta:
        unique_together = ('market_day', 'stall', 'vendor')
