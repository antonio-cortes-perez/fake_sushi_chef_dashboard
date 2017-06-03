from rest_framework import authentication, permissions, viewsets
from .models import RunEvent
from .serializers import RunEventSerializer


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


class RunEventViewSet(DefaultMixin, viewsets.ModelViewSet):
    queryset = RunEvent.objects.order_by('channel_id')
    serializer_class = RunEventSerializer
