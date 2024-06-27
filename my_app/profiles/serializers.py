from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from .models import Profile

class ProfileCreationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['username', 'password', 'email', 'bio'],

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(ProfileCreationSerializer, self).create(validated_data)