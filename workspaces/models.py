from datetime import timezone

from django.db import models


# Create your models here.
class Workspace(models.Model):
    name = models.CharField(max_length=200, default='Nuevo espacio de trabajo')
    description = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
