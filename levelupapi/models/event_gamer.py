from django.db import models


class EventGamer(models.Model):
    """EventGamer model class"""
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    gamer = models.ForeignKey('Gamer', on_delete=models.CASCADE)