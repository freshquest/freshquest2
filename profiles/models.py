from django.db import models
import uuidfield

class VendorProfile(models.Model):
    vendor = models.OneToOneField('slotting.Vendor')
    categories = models.ManyToManyField('Category', blank=True)
    website = models.URLField(help_text='Website', blank=True)
    accepts_preorders = models.BooleanField(default=False)

class Category(models.Model):
    category_id = uuidfield.UUIDField(auto=True, unique=True, editable=False)
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
