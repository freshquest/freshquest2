from rest_framework import serializers
from project.serializers import CoercibleSlugRelatedField
from .models import MarketDay
from .models import Vendor
from .models import Assignment
from .models import Stall


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor


class MarketDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketDay


class StallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stall


class AssignmentSerializer(serializers.ModelSerializer):
    market_day_id = CoercibleSlugRelatedField(source='market_day', many=False, slug_field='market_day_id', required=True)
    stall_id = CoercibleSlugRelatedField(source='stall', many=False, slug_field='stall_id', required=True)
    vendor_id = CoercibleSlugRelatedField(source='vendor', many=False, slug_field='vendor_id', required=True)

    class Meta:
        model = Assignment
        fields = ['assignment_id', 'market_day_id', 'stall_id', 'vendor_id', 'is_checked_in']
