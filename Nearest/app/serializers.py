from rest_framework import serializers
from .models import UserLocation

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocation
        fields = '__all__'