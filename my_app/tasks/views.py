# Create your views here.
from django.http import JsonResponse
from django.core.serializers import serialize

from .models import Task, User

def index(request):
    tasks = Task.objects.all()
    data = serialize('python', tasks)
    return JsonResponse(data, safe=False)

def users(request):
    users = User.objects.all()
    data = serialize('python', users)
    return JsonResponse(data, safe=False)
