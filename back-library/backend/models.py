from django.db import models
from django.contrib. auth.models import User

# Create your models here.

class Perfil(models.Model):
    TIPO_PERFIL = [
        ('leitor', 'Leitor'),
        ('admin', 'Administrador')
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil")
    tipo = models.CharField(max_length=20, choices=TIPO_PERFIL)
    telefone = models.CharField(max_length=20, null=True, blank=True, verbose_name="Telefone")
    fotoPerfil = models.ImageField(upload_to='perfil', null=True, blank=True, verbose_name="Foto de Perfil")

    def __str__(self):
        return f'{self.usuario}'


class Autor(models.Model):
    GENERO = [
        ('F', 'Feminino'),
        ('M', 'Masculino')
    ]

    nome = models.CharField(max_length=150, verbose_name='Autor')
    dataNascimento = models.DateField(verbose_name='Data de Nascimento')
    dataNascimento = models.DateField(verbose_name='Data de Nascimento', null=True, blank=True)
    genero = models.CharField(max_length=1, choices=GENERO, blank=True)
    
    def __str__(self):
        return f'{self.nome}'
    

class Genero(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Gênero')

    def __str__(self):
        return f'{self.nome}'


class Linguagem(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Linguagem')

    def __str__(self):
        return f'{self.nome}'
    

class Editora(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Editora')
    
    def __str__(self):
        return f'{self.nome}'


class Status(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Status')
    
    def __str__(self):
        return f'{self.nome}'


class Livro(models.Model):
    nome = models.CharField(max_length=200, verbose_name='Título')
    status = models.CharField()
    
    def __str__(self):
        return f'{self.nome}'

class Emprestimo(models.Model):
    STATUS = [
        ('M', 'Manutenção'),
        ('D', 'Disponível'),
        ('E', 'Emprestado'),
        ('R', 'Reservado')
    ]

    livro = models.ForeignKey(Livro, on_delete=models.RESTRICT, related_name='Empréstimo')
    dataEntrega = models.DateField(verbose_name='Data de devolução')
    status = models.CharField(max_length=1, choices=STATUS, default='M', help_text='Status do Livro')

    def __str__(self):
        return f'{self.livro}'
    
class Lista(models.Model):
    tipo = models.CharField()

    def __str__(self):
        return f'{self.tipo}'
    
