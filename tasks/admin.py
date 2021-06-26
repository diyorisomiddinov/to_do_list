from django.contrib import admin

from tasks.models import TaskModel


@admin.register(TaskModel)
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']
