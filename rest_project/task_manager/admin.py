from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("task", "assignee", "date", "priority")
    list_filter = ("assignee", "priority", "date")
    search_fields = ("task", "assignee")
