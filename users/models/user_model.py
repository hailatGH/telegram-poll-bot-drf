from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

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

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)