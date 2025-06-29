from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from datetime import timedelta
from .models import User, Kudos
from .serializers import UserSerializer, KudosSerializer

class LoginView(views.APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'success': True})
        return Response({'error': 'Invalid credentials'}, status=400)

class LogoutView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        logout(request)
        return Response({'success': True})

class MeView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        return Response(UserSerializer(request.user).data)

class UsersInOrgView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    def get_queryset(self):
        return User.objects.filter(organization=self.request.user.organization).exclude(id=self.request.user.id)

class KudosReceivedView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = KudosSerializer
    def get_queryset(self):
        return Kudos.objects.filter(receiver=self.request.user).order_by('-created_at')

class KudosGivenView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = KudosSerializer
    def get_queryset(self):
        return Kudos.objects.filter(giver=self.request.user).order_by('-created_at')

class KudosRemainingView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        now = timezone.now()
        week_start = now - timedelta(days=now.weekday())
        kudos_this_week = Kudos.objects.filter(
            giver=request.user,
            created_at__gte=week_start
        ).count()
        return Response({'remaining': max(0, 3 - kudos_this_week)})

class GiveKudosView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        receiver_id = request.data.get('receiver_id')
        message = request.data.get('message')
        now = timezone.now()
        week_start = now - timedelta(days=now.weekday())
        kudos_this_week = Kudos.objects.filter(
            giver=request.user,
            created_at__gte=week_start
        ).count()
        if kudos_this_week >= 3:
            return Response({'error': 'No kudos left this week.'}, status=400)
        try:
            receiver = User.objects.get(id=receiver_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=404)
        if receiver.organization != request.user.organization or receiver == request.user:
            return Response({'error': 'Invalid recipient.'}, status=400)
        kudo = Kudos.objects.create(giver=request.user, receiver=receiver, message=message)
        return Response(KudosSerializer(kudo).data, status=201)