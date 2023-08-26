from rest_framework import serializers

from .models import Tasks

class TasksSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tasks
        fields = ("owner", "title", "body")


class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tasks
        fields = ("title", "body", "created", "status")
