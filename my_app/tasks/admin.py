from django.contrib import admin

# Register your models here.

from .models import Task
from rest_framework.authtoken.admin import TokenAdmin

admin.site.register(Task)
