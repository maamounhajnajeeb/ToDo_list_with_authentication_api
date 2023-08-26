from rest_framework import generics

from django.shortcuts import render

from .serializers import TasksSerializer, TaskSerializer
from .permissions import IsAuthorOrReadOnly
from .models import Tasks
from .new_request import Request


class TasksView(generics.ListCreateAPIView):
    serializer_class = TasksSerializer
    queryset = Tasks.objects.all()
    
    def post(self, request, *args, **kwargs):
        new_request = Request(request, self.request.user)
        new_request.to_dict()
        return super().post(new_request, *args, **kwargs)
    
def create_task(request):
    return render(request, "create_task.html", {})


class SpecificTask(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Tasks.objects.all()
    
    def get_object(self):
        return self.queryset.get(id=self.kwargs['id'])