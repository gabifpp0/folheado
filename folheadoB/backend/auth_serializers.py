from rest_framework import serializers
from .models import Perfil
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from django.db import transaction

def get_user_type(usuario):
    if hasattr(usuario.tipo_perfil, 'leitor'):
        return 'Leitor' , usuario.tipo_perfil.perfil.tipo
    elif hasattr(usuario.tipo_perfil, 'admnin'):
        return 'Administrador' , usuario.tipo_perfil.perfil.tipo
    else:
        return 'Unknown', None
 
class ResgistroPerfil(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128, write_only=True)
    email = serializers.EmailField()    
    tipo = serializers.ChoiceField(choices=Perfil.TIPO_PERFIL)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=150)
    telefone = serializers.CharField(max_length=20, required=False, allow_blank=True)

    @transaction.atomic
    def create(self, validated_data):

            username = validated_data.pop('username')
            password = validated_data.pop('password')
            email = validated_data.pop('email')
            first_name = validated_data.pop('first_name')
            last_name = validated_data.pop('last_name')
            telefone = validated_data.pop('telefone', '')

            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name
            )

            perfil = Perfil.objects.create(
                usuario=user,
                tipo=validated_data.get('tipo'),
                telefone=telefone
            )

            return perfil
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        user = self.user
        user_type_display, user_type = get_user_type(user)

        data.update({
             'user_id': user.id,
             'username': user.username,
             'email': user.email,
        })

        data['tipo'] = user_type_display

        return data