from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'channels', views.ContentChannelViewSet)
router.register(r'channelruns', views.ChannelRunViewSet)
router.register(r'stages', views.EventViewSet)
router.register(r'logs', views.LogViewSet)