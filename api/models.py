import uuid

from django.db import models


class ContentChannel(models.Model):
    """
    The sushibar contect channel representation.
    """
    # id = local, implicit, autoincrementing integer primary key
    channel_id = models.UUIDField('The id from contentcuration.models.Channel')
    name = models.CharField(max_length=200, blank=True)  # equiv to ricecooker's `title`
    description = models.CharField(max_length=400, blank=True)
    version = models.IntegerField(default=0)
    source_domain = models.CharField(max_length=300, blank=True, null=True)
    source_id = models.CharField(max_length=200, blank=True, null=True)

    # User-related fields (the person who registered the channel with sushibar)
    user_registered_by = models.EmailField(max_length=200, blank=True, null=True)
    user_token = models.CharField(max_length=200, blank=True, null=True)

    # Content curation related fields
    content_server = models.URLField(max_length=300, default='https://develop.contentworkshop.learningequality.org')

    def __str__(self):
        return '<Channel ' + self.channel_id.hex[:8] + '...>'


class ContentChannelRun(models.Model):
    """
    A particular sushi chef run for the content channel `channel`.
    """
    run_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    channel = models.ForeignKey(ContentChannel, on_delete=models.CASCADE, related_name='runs')
    chef_name = models.CharField(max_length=200)
    ricecooker_version = models.CharField(max_length=100, blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)

    def __str__(self):
        return '<Run ' + self.run_id.hex[:8] + '...>'


class ChannelRunStage(models.Model):
    run_id = models.ForeignKey(ContentChannelRun, on_delete=models.CASCADE, related_name='stages')
    stage = models.CharField(max_length=100)
    duration = models.FloatField(default=0)

    def __str__(self):
        return '<Event for run ' + self.run_id.hex[:8] + '...>'


class Log(models.Model):
    run_id = models.ForeignKey(ContentChannelRun, on_delete=models.CASCADE, related_name='logs')
    created = models.FloatField()
    message = models.TextField()

    def __str__(self):
        return '%s: %s : %s : %s' % (self.id, self.run_id, self.created, self.message)
