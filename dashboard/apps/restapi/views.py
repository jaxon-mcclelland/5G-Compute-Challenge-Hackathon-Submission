from ..main.models import iotDevice
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import iotDeviceSerializer

class iotDeviceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows iotDevices to be viewed or edited.
    """
    queryset = iotDevice.objects.all().order_by('-created_at')
    serializer_class = iotDeviceSerializer
    permission_classes = [permissions.IsAuthenticated]