from django.shortcuts import render
from django.views.generic.base import View

from contatos.models import Pessoa

# Create your views here.


class ContatoListView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        contexto = { 'pessoas': pessoas, }
        return render(request, 'contatos/listaContatos.html', contexto)

def buscaUmContato(request):
    return render(request, 'contatos/buscaUmContato.html')

def respostaBuscaUmContato(request):
    pessoas = Pessoa.objects.all().filter(nome__icontains=request.GET.get('nome'))
    contexto = { 'pessoas': pessoas, }
    return render(request, 'contatos/listaContatos.html', contexto)
