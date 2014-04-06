from rest_framework import serializers

class CoercibleSlugRelatedField(serializers.SlugRelatedField):
    """
    Use this custom field when you want to represent a relationship to another object
    using its UUID, or something else, not a string, which can be cocerced to a string.
    """
    def to_native(self, value):
        return str(getattr(value, self.slug_field))
