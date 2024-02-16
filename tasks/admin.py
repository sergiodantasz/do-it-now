from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'user']
    list_display_links = ['id']
    list_editable = ['name']
    list_filter = ['user']
    list_per_page = 15
    search_fields = ['name', 'user']
    ordering = ['-id']
