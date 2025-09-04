from django.shortcuts import render
from django.views.generic.base import View
from contatos.models import Pessoa

# Create your views here.

class ContatoListView(View):
    def get(self, request, *args, **kwargs):
        # recupera todas as pessoas do banco de dados
        pessoas = Pessoa.objects.all()  

        # contexto para o template
        # dicionário contexto
        # chave 'pessoas'
        # valor da chave é o objecto com todas as pessoas
        contexto = {'pessoas': pessoas}
        return render(request, 'pessoas/listaContatos.html', contexto)
