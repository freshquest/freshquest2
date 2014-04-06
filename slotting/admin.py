from django.contrib import admin
from slotting.models import Vendor
from slotting.models import MarketDay
from slotting.models import Stall
from profiles.models import VendorProfile
from slotting.models import Assignment

class VendorProfileInline(admin.StackedInline):
    model = VendorProfile

class VendorAdmin(admin.ModelAdmin):
    inlines = (VendorProfileInline,)

class StallAdmin(admin.ModelAdmin):
    model = Stall
    list_display = ('building', 'section', 'stall_number')
    ordering = ('building', 'section', 'stall_number')


admin.site.register(Vendor, VendorAdmin)
admin.site.register(MarketDay)
admin.site.register(Stall, StallAdmin)
admin.site.register(Assignment)
