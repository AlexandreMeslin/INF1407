from django.shortcuts import render

# Create your views here.

from contatos.models import Pessoa
from django.views.generic.base import View
from contatos.forms import ContatoModel2Form
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy

class ContatoListView(View):
    def get(self, request):
        pessoas = Pessoa.objects.all()  # Recupera todas as pessoas do banco de dados
        contexto = {
            'pessoas': pessoas,
        }
        return render(request, 'contatos/listaContatos.html', contexto)

class ContatoCreateView(View):
    def get(self, request):
        contexto = {'formulario': ContatoModel2Form()}
        return render(request, 'contatos/criaContato.html', contexto)

    def post(self, request):
        formulario = ContatoModel2Form(request.POST)    # Cria um formulário preenchido com os dados enviados pelo usuário
        if formulario.is_valid():                       # Verifica se os dados do formulário são válidos
            formulario.save()                           # Salva o novo contato no banco de dados
            return HttpResponseRedirect(reverse_lazy('contatos:lista-contatos'))
        else:
            contexto = {'formulario': formulario}
            return render(request, 'contatos/criaContato.html', contexto)

class ContatoUpdateView(View):
    def get(self, request, pk):
        pessoa = Pessoa.objects.get(pk=pk)              # Recupera a pessoa do banco de dados com a chave primária fornecida
        formulario = ContatoModel2Form(instance=pessoa) # Cria um formulário preenchido com os dados da pessoa
        contexto = {'pessoa': formulario}               # Prepara o contexto com o formulário
        return render(request, 'contatos/atualizaContato.html', contexto)

    def post(self, request, pk):
        pessoa = Pessoa.objects.get(pk=pk)                              # Recupera a pessoa do banco de dados com a chave primária fornecida
        formulario = ContatoModel2Form(request.POST, instance=pessoa)   # Cria um formulário preenchido com os dados enviados pelo usuário e a instância da pessoa
        if formulario.is_valid():                                       # Verifica se os dados do formulário são válidos
            formulario.save()                                           # Salva as alterações no banco de dados
            return HttpResponseRedirect(reverse_lazy('contatos:lista-contatos'))
        else:
            contexto = {'pessoa': formulario}               # Prepara o contexto com o formulário preenchido com os dados inválidos
            return render(request, 'contatos/atualizaContato.html', contexto)

class ContatoDeleteView(View):
    def get(self, request, pk):
        pessoa = Pessoa.objects.get(pk=pk)              # Recupera a pessoa do banco de dados com a chave primária fornecida
        contexto = {'pessoa': pessoa}                   # Prepara o contexto com a pessoa a ser deletada
        return render(request, 'contatos/apagaContato.html', contexto)

    def post(self, request, pk):
        pessoa = Pessoa.objects.get(pk=pk)              # Recupera a pessoa do banco de dados com a chave primária fornecida
        pessoa.delete()                                 # Deleta a pessoa do banco de dados
        return HttpResponseRedirect(reverse_lazy('contatos:lista-contatos'))
        