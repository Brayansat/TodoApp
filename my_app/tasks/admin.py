from django.contrib import admin

# Register your models here.

from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description", "priority", "user", "completed"]
    search_fields = ["name"]
