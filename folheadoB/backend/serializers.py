from rest_framework import serializers
from .models import Perfil, Autor, Genero, Linguagem, Editora, Livro, Emprestimo, ListaLeitura
from django.contrib.auth.models import User

class UserPerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class PerfilSerializer(serializers.ModelSerializer):    
    usuario = UserPerfilSerializer(read_only=True)

    class Meta:
        model = Perfil
        fields = ['id', 'usuario', 'tipo', 'telefone', 'fotoPerfil']

class AutorSerializer(serializers.ModelSerializer):    
    #adicionar validação de dataFalecimento > dataNascimento depois
    
    class Meta:
        model = Autor
        fields = ['nome', 'dataNascimento', 'dataFalecimento', 'genero']

class GeneroSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Genero
        fields = ['nome']

class LinguagemSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Linguagem
        fields = ['nome']

class EditoraSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Editora
        fields = ['nome']

class LivroSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Livro
        fields = ['nome', 'autor', 'genero', 'linguagem', 'editora']

class EmprestimoSerializer(serializers.ModelSerializer):    
    leitor = serializers.PrimaryKeyRelatedField(queryset=Perfil.objects.all(), write_only=True)
    leitor_dados = PerfilSerializer(source='leitor',read_only=True)
    
    livro = serializers.PrimaryKeyRelatedField(queryset=Livro.objects.all(), write_only=True)
    livro_dados = LivroSerializer(source='livro',read_only=True)
    
    #Permite a relação e seleção pelo ID do Perfil
    #adicionar validação de dataDevolucao > dataEmprestimo depois
    #adicionar validação de status depois - ex: não permitir mudar para 'D' se já estiver 'R', etc.
    #se o livro já estiver emprestado, não permitir novo empréstimo
    #se o livro estiver reservado por outro usuário, não permitir novo empréstimo
    #se o livro estiver em manutenção, não permitir novo empréstimo
    #se o livro for devolvido, atualizar status para 'D'
    #se o livro for emprestado, atualizar status para 'E'

    class Meta:
        model = Emprestimo
        fields = ['leitor', 'leitor_dados', 'livro', 'livro_dados', 'dataEmprestimo', 'dataDevolucao', 'status']

class ListaLeituraSerializer(serializers.ModelSerializer):    
    leitor = serializers.PrimaryKeyRelatedField(queryset=Perfil.objects.all(), write_only=True)
    leitor_dados = PerfilSerializer(source='leitor',read_only=True)
    
    livro = serializers.PrimaryKeyRelatedField(queryset=Livro.objects.all(), write_only=True)
    livro_dados = LivroSerializer(source='livro',read_only=True)
    
    
    class Meta:
        model = ListaLeitura
        fields = ['leitor', 'leitor_dados', 'livro', 'livro_dados']