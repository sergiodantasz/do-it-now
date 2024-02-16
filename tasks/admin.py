from django.contrib import admin

from django_admin_relation_links import AdminChangeLinksMixin

from .models import Task


@admin.register(Task)
class TaskAdmin(AdminChangeLinksMixin, admin.ModelAdmin):
    list_display = ['id', 'name', 'user_link']
    list_display_links = ['id']
    list_editable = ['name']
    list_filter = ['user']
    list_per_page = 15
    search_fields = ['name', 'user']
    ordering = ['-id']
    change_links = ['user']
