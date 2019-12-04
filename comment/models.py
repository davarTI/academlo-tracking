from django.db import models
from datetime import timezone
from django.contrib.auth.models import User
from task.models import Task
# from core.models import User

# Create your models here.
class Comment(models.Model):
    responsible_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    # deleted_at = 