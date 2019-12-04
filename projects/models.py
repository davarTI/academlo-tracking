from datetime import timezone

from django.db import models


# Create your models here.
from workspaces.models import Workspace


class Project(models.Model):
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=350)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name