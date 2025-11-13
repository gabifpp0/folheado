from django.contrib import admin
from .models import Perfil, Autor, Genero, Linguagem, Editora, Livro, Emprestimo, ListaLeitura
# Register your models here.

admin.site.register(Perfil)
admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Linguagem)
admin.site.register(Editora)
admin.site.register(Livro)
admin.site.register(Emprestimo)
admin.site.register(ListaLeitura)
