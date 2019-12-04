from rest_framework import serializers

from workspaces.models import Workspace


class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields =('id', 'name', 'description', 'created_at')