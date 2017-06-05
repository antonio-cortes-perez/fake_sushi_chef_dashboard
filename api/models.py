from django.db import models


# Create your models here.
class RunEvent(models.Model):
    channel_id = models.CharField(max_length=100)
    event = models.CharField(max_length=100)
    timestamp = models.DateTimeField()

    def __str__(self):
        return '%s : %s : %s' % (self.timestamp, self.channel_id, self.event)
