from django.shortcuts import render

# Create your views here.

from contatos.models import Pessoa
from django.views.generic.base import View

class ContatoListView(View):
    def get(self, request):
        pessoas = Pessoa.objects.all()
        contexto = {
            'pessoas': pessoas,
        }
        return render(request, 'contatos/listaContatos.html', contexto)
