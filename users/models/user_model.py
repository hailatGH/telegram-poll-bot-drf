from django.db import models
from django.contrib.auth.models import AbstractUser

from .timestamp_model import TimestampModel
from utils.validators import validate_image
from utils.file_dir import Users_Profile_Images

class CustomUser(TimestampModel, AbstractUser):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    phone_number = models.CharField(blank=True, null=True, max_length=13)
    email_verified = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to=Users_Profile_Images, blank=True, null=True, validators=[validate_image])