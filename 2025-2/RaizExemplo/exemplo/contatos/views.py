from django.shortcuts import render
from django.views.generic.base import View
from contatos.models import Pessoa
from contatos.forms import ContatoModel2Form

# Create your views here.

class ContatoCreateView(View):
    def get(self, request, *args, **kwargs):
        contexto = {'form': ContatoModel2Form, }
        return render(request, 'contatos/cadastroContato.html', contexto)

class ContatoListView(View):
    def get(self, request, *args, **kwargs):
        # recupera todas as pessoas do banco de dados
        pessoas = Pessoa.objects.all().order_by('nome')

        # contexto para o template
        # dicionário contexto
        # chave 'pessoas'
        # valor da chave é o objecto com todas as pessoas
        contexto = {'pessoas': pessoas}
        return render(request, 'contatos/listaContatos.html', contexto)
