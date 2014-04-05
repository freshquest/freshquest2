from rest_framework import mixins, viewsets
from slotting.serializers import VendorSerializer
from slotting.serializers import MarketDaySerializer
from slotting.models import MarketDay
from slotting.models import Vendor


class VendorViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    lookup_field = 'vendor_id'
    lookup_field_regex = '[0-9a-f]{32}'
    model = Vendor
    serializer_class = VendorSerializer


class MarketDayView(mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):
    model = MarketDay
    serializer_class = MarketDaySerializer

    def get_object(self):
        '''
        Like GenericAPIView.get_object, raises django.http.Http404
        when the object does not exist.
        '''
        return self.model.objects.first()

