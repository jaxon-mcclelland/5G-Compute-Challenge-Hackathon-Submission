from rest_framework import serializers
from ..main.models import iotDevice

# Main Models Serializer
class iotDeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = iotDevice
        fields = ['deviceHostname', 'deviceTemperature', 'deviceHumidity', 'devicePressure', 'deviceMagX', 'deviceMagY', 'deviceMagZ']