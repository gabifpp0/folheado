from backend.auth_serializers import CustomTokenObtainPairSerializer, ResgistroPerfil
from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomTokenObtainPairSerializer

class RegistroPerfilView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ResgistroPerfil

    def token(self, request):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            perfil = serializer.save()
            
            token = CustomTokenObtainPairSerializer.get_token(perfil.usuario)

            return Response({
                'token': str(token.access_token),
                'refresh': str(token),
                'user': serializer.data,
                'tipo': perfil.tipo,
            }, status=201)
        
        return Response(serializer.errors, status=400)