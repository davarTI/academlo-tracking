from django.urls import path, include
from rest_framework import routers

from core.views import UserViewSet
from board.views import BoardViewSet
from task.views import TaskViewSet
from comment.views import CommentViewSet

routers = routers.DefaultRouter()
routers.register(r'users', UserViewSet)
routers.register(r'boards', BoardViewSet)
routers.register(r'tasks', TaskViewSet)
routers.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(routers.urls))
]