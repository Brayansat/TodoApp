from django.db import models
from django.contrib.auth.models import AbstractUser

class Profile(AbstractUser):
    bio = models.TextField(verbose_name="Biography", null=True, blank=True)
