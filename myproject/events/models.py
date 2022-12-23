from django.db import models

class EventTab(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=128)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    category = models.CharField(max_length=20)
    location = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'event_tab'

class EventCommentTab(models.Model):
    id = models.BigAutoField(primary_key=True)
    event_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=20)
    comment = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'event_comment_tab'


class EventImagesTab(models.Model):
    id = models.BigAutoField(primary_key=True)
    event_id = models.PositiveBigIntegerField()
    image = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'event_images_tab'


class EventLikesTab(models.Model):
    id = models.BigAutoField(primary_key=True)
    event_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'event_likes_tab'


class EventParticipantTab(models.Model):
    id = models.BigAutoField(primary_key=True)
    event_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'event_participant_tab'

