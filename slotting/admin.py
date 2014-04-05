from django.contrib import admin
from slotting.models import Vendor
from profiles.models import VendorProfile

class VendorProfileInline(admin.StackedInline):
    model = VendorProfile

class VendorAdmin(admin.ModelAdmin):
    inlines = (VendorProfileInline,)

admin.site.register(Vendor, VendorAdmin)
