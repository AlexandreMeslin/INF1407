from django.contrib import admin

# Register your models here.

from contatos.models import Pessoa

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'idade', 'salario', 'email', 'telefone', 'dtNasc')
    search_fields = ('nome', 'email')
    list_filter = ('idade',)