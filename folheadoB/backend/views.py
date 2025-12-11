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

    #def get_queryset(self):
        #return Perfil.objects.all()
    
    """@action(detail=False, methods=['get'])
    def perfil(self,request):
        usuario = request.user.perfil

        data = {
            'username': usuario.perfil.username,
            'email': usuario.perfil.email,
            'first_name': usuario.perfil.first_name,
            'last_name': usuario.perfil.last_name,
            'tipo': usuario.tipo,
        }
        
        return Response(data)"""

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    #permission_classes = [permissions.IsAuthenticated]

    """@action(detail=False, methods=['get'])
    def get_queryset(self):
        return Autor.objects.all()
    """
    
class GeneroViewSet(viewsets.ModelViewSet):
    #queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    #permission_classes = [permissions.IsAuthenticated]

    #Não é necessário definir queryset aqui se for usar o get_queryset

    def get_queryset(self):
        return Genero.objects.all()
    
class LinguagemViewSet(viewsets.ModelViewSet):
    queryset = Linguagem.objects.all()
    serializer_class = LinguagemSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Linguagem.objects.all()
    
class EditoraViewSet(viewsets.ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Editora.objects.all()

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Livro.objects.all()

class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Emprestimo.objects.all()

class ListaLeituraViewSet(viewsets.ModelViewSet):
    queryset = ListaLeitura.objects.all()
    serializer_class = ListaLeituraSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ListaLeitura.objects.all()
