import django_filters
from .models import Task


class TaskFilter(django_filters.FilterSet):
    completed = django_filters.BooleanFilter(field_name="completed")
    priority = django_filters.CharFilter(field_name="priority", lookup_expr="exact")

    class Meta:
        model = Task
        fields = ["completed", "priority"]
