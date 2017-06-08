from rest_framework import serializers
from .models import ContentChannel, ContentChannelRun, ChannelRunStage, Log


class ContentChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentChannel
        fields = ('id', 'channel_id', 'name', 'description', 'version',
                  'source_domain', 'source_id', 'user_registered_by',
                  'user_token', 'content_server')


class ChannelRunSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentChannelRun
        fields = ('run_id', 'channel', 'chef_name', 'ricecooker_version', 'duration')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelRunStage
        fields = ('id', 'run_id', 'stage', 'duration',)


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ('id', 'run_id', 'created', 'message',)
