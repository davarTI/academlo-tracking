from django.db import models
from django.utils import timezone
from projects.models import Project
# Libreríaspara borrado lógico
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE

class Board(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    position = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
