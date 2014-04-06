from rest_framework import mixins, viewsets
from slotting.serializers import VendorSerializer
from slotting.serializers import MarketDaySerializer
from slotting.serializers import AssignmentSerializer
from slotting.serializers import StallSerializer
from slotting.models import Assignment
from slotting.models import MarketDay
from slotting.models import Stall
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


class StallViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    lookup_field = 'assignment_id'
    lookup_field_regex = '[0-9a-f]{32}'
    model = Stall
    serializer_class = StallSerializer


class AssignmentViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    lookup_field = 'assignment_id'
    lookup_field_regex = '[0-9a-f]{32}'
    model = Assignment
    serializer_class = AssignmentSerializer
