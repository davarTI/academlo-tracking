from django.db import models
from django.contrib.auth.models import User
from board.models import Board
# from core.models import User

# Create your models here.
class Task(models.Model):
    responsible_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    due_date = models.DateTimeField(auto_now_add=True)
    position = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
