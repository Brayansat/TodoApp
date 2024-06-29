from rest_framework import generics, permissions
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from .serializers import ProfileCreationSerializer
from .models import Profile

class ProfileDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileCreationSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'  # Ajusta según tu modelo de perfil

    def get_object(self):
        id = self.kwargs.get('id')
        if not id:
            raise AssertionError('Expected view ProfileDetailView to be called with a URL keyword argument named "id".')
        return Profile.objects.get(id=id)
    

class ProfileCreationView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = ProfileCreationSerializer
    permission_classes = [AllowAny]

# Create your views here.
