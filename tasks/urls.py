from django.urls import path

from .views import create_task, mark_task_as_done, tasks

app_name = 'tasks'

urlpatterns = [
    path('', tasks, name='tasks'),
    path('done/', mark_task_as_done, name='done'),
    path('create/', create_task, name='create'),
]
