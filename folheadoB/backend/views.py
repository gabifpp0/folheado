from django.shortcuts import render
from .models import Perfil, Autor, Genero, Linguagem, Editora, Livro, Emprestimo, ListaLeitura
from .serializers import PerfilSerializer, AutorSerializer, GeneroSerializer, LinguagemSerializer, EditoraSerializer, LivroSerializer, EmprestimoSerializer, ListaLeituraSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.

class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Perfil.objects.all()
    
    @action(detail=False, methods=['get'])
    def perfil(self,request):
        proponente = request.user.perfil

        data = {
            'usuario': proponente.username,
            'dataNascimento': proponente.perfil.dataNascimento,
            'telefone': proponente.perfil.telefone,
            'endereco': proponente.perfil.endereco
        }
        
        return Response(data)

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Autor.objects.all()
    
