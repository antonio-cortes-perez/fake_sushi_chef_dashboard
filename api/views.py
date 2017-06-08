from rest_framework import authentication, permissions, viewsets
from .models import ContentChannel, ContentChannelRun, ChannelRunStage, Log
from .serializers import ContentChannelSerializer, ChannelRunSerializer, EventSerializer, LogSerializer


class DefaultMixin(object):
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class ContentChannelViewSet(DefaultMixin, viewsets.ModelViewSet):
    queryset = ContentChannel.objects.order_by('id')
    serializer_class = ContentChannelSerializer


class ChannelRunViewSet(DefaultMixin, viewsets.ModelViewSet):
    queryset = ContentChannelRun.objects.order_by('run_id')
    serializer_class = ChannelRunSerializer


class EventViewSet(DefaultMixin, viewsets.ModelViewSet):
    queryset = ChannelRunStage.objects.order_by('id')
    serializer_class = EventSerializer


class LogViewSet(DefaultMixin, viewsets.ModelViewSet):
    queryset = Log.objects.order_by('id')
    serializer_class = LogSerializer
