from django.db import models
from django.conf import settings

class Device(models.Model):
    SENSOR = "sensor"
    ACTUATOR = "actuator"
    DEVICE_TYPES = [
        (SENSOR, "Sensor"),
        (ACTUATOR, "Actuator"),
    ]

    name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=20, choices=DEVICE_TYPES)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="devices"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.device_type})"
