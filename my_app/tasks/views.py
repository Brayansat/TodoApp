# Create your views here.
from .models import Task
from rest_framework import viewsets
from .serializers import TaskSerializer, TaskListSerializer, TaskUpdateSerializer
from .filters import TaskFilter
from django_filters.rest_framework import DjangoFilterBackend


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter

    def get_queryset(self):
        return self.request.user.tasks.all()

    def get_serializer_class(self):
        if self.action == "list":
            return TaskListSerializer
        elif self.action == "create":
            return TaskSerializer
        elif self.action in ["update", "partial_update"]:
            return TaskUpdateSerializer
        return TaskListSerializer

    def perform_destroy(self, instance):
        instance.delete()
