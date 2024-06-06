# Create your views here.
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from .models import Task
from .serializers import TaskSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class TaskviewSet(viewsets.ModelViewSet):
    queryset= Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [OrderingFilter]
    Ordering_fields = ['priority']

    def get_queryset(self):
        queryset = Task.objects.all()
        username = self.request.query_params.get('username')
        if username is not None:
            queryset = queryset.filter(purchaser__username=username)
        return queryset