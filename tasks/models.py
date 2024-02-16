from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    name = models.CharField(unique=True, blank=False, max_length=250)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
