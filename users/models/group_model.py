from django.contrib.auth.models import Group as AuthGroup
from django.db import models
from .timestamp_model import TimestampModel

class CustomGroup(TimestampModel, AuthGroup):
    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    description = models.CharField(blank=True, null=True, max_length=1024)