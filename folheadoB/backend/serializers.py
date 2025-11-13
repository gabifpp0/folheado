from rest_framework import serializers
from .models import Perfil, Autor, Genero, Linguagem, Editora, Livro, Emprestimo, ListaLeitura


class PerfilSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Perfil
        fields = ['usuario', 'dataNascimento', 'telefone', 'endereco']

class AutorSerializer(serializers.ModelSerializer):    
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
    autor = AutorSerializer(read_only=True)
    genero = GeneroSerializer(read_only=True)
    linguagem = LinguagemSerializer(read_only=True)
    editora = EditoraSerializer(read_only=True)

    class Meta:
        model = Livro
        fields = ['nome', 'autor', 'genero', 'linguagem', 'editora']

class EmprestimoSerializer(serializers.ModelSerializer):    
    livro = LivroSerializer(read_only=True)
    usuario = PerfilSerializer(read_only=True)
    
    class Meta:
        model = Emprestimo
        fields = ['livro', 'usuario', 'dataEmprestimo', 'dataDevolucao', 'status']

class ListaLeituraSerializer(serializers.ModelSerializer):    
    leitor = PerfilSerializer(read_only=True)
    livro = LivroSerializer(read_only=True)
    
    class Meta:
        model = ListaLeitura
        fields = ['leitor', 'livro']