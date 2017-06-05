from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import RunEvent


class RunEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunEvent
        fields = ('channel_id', 'event', 'timestamp',)
