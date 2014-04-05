from rest_framework import mixins, viewsets
from slotting.serializers import VendorSerializer
from slotting.models import Vendor


class VendorViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    lookup_field = 'vendor_id'
    lookup_field_regex = '[0-9a-f]{32}'
    model = Vendor
    serializer_class = VendorSerializer
