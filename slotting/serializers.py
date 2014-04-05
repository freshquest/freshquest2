from rest_framework import serializers
from .models import MarketDay
from .models import Vendor
from .models import Assignment


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor


class MarketDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketDay


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
