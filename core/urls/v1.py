from django.urls import path, include
from rest_framework import routers

from core.views import UserViewSet
# from academlo_tracking.views import BoardViewSet

routers = routers.DefaultRouter()
routers.register(r'users', UserViewSet)
# routers.register(r'boards', BoardViewSet)

urlpatterns = [
    path('', include(routers.urls))
]