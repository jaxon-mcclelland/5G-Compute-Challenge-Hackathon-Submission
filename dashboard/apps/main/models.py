from django.db import models

# Create your models here.
class iotDevice(models.Model):
    deviceHostname = models.CharField(max_length = 10)
    deviceTemperature = models.FloatField()
    deviceHumidity = models.FloatField()
    devicePressure = models.FloatField()
    deviceMagX = models.FloatField()
    deviceMagY = models.FloatField()
    deviceMagZ = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.deviceHostname
