from django.contrib.auth.models import Permission as AuthPermission
from .timestamp_model import TimestampModel

class CustomPermission(TimestampModel, AuthPermission):
    class Meta:
        verbose_name = "Permission"
        verbose_name_plural = "Permissions"

