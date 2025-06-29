from rest_framework import serializers
from .models import User, Organization, Kudos

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'organization']

class KudosSerializer(serializers.ModelSerializer):
    giver = UserSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)
    class Meta:
        model = Kudos
        fields = ['id', 'giver', 'receiver', 'message', 'created_at']