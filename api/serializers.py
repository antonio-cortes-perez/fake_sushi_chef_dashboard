from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import RunEvent


class RunEventSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()  # by default points to get_links

    class Meta:
        model = RunEvent
        fields = ('channel_id', 'event', 'timestamp', 'links', )

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('run_event-detail', kwargs={'pk':obj.pk}, request=request)
        }