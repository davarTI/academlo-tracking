from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class Board(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=150)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
