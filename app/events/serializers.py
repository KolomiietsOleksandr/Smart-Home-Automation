from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id", "device", "event_type", "value", "timestamp"]
        read_only_fields = ["id", "timestamp"]
