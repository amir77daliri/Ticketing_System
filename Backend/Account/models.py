from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Q
import os


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f'{instance.username}-{ext}'
    return f'Account/profile_images/{final_name}'


class User(AbstractUser):
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(upload_to=upload_image_path, blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    is_admin = models.BooleanField(default=False, blank=True)

    def __str__(self):
        if self.first_name and self.last_name:
            return self.get_full_name()
        return self.username
