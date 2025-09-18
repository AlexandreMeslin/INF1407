from django.shortcuts import render
from django.views.generic.base import View
from contatos.models import Pessoa
from contatos.forms import ContatoModel2Form
from django.http import HttpResponseRedirect
from django.urls.base import reverse_lazy

# Create your views here.

class ContatoDeleteView(View):
    '''
    Classe para apagar um contato
    '''
    def get(self, request, pk, *args, **kwargs):
        '''
        Exibe a página de confirmação de exclusão
        '''
        pessoa = Pessoa.objects.get(pk=pk) # recupera a pessoa do banco de dados
        contexto = {'pessoa': pessoa, }
        return render(request, 'contatos/confirmaExclusao.html', contexto)

    def post(self, request, pk, *args, **kwargs):
        '''
        Apaga o contato
        '''
        pessoa = Pessoa.objects.get(pk=pk) # recupera a pessoa do banco de dados
        pessoa.delete() # apaga a pessoa do banco de dados
        return HttpResponseRedirect(reverse_lazy('contatos:lista-contatos')) # redireciona para a lista de contatos

class ContatoUpdateView(View):
    '''
    Classe para atualizar um contato
    '''
    def get(self, request, pk, *args, **kwargs):
        '''
        Exibe o formulário de atualização
        '''
        pessoa = Pessoa.objects.get(pk=pk) # recupera a pessoa do banco de dados
        form = ContatoModel2Form(instance=pessoa) # cria o formulário com os dados da pessoa
        contexto = {
            'form': form,
            'titulo_janela': 'Atualização de Contato',
            'titulo_pagina': 'Atualiza Contato',
            'botao': 'Atualizar',
        }
        return render(request, 'contatos/formContato.html', contexto)

    def post(self, request, pk, *args, **kwargs):
        '''
        Atualiza um contato
        '''
        pessoa = Pessoa.objects.get(pk=pk) # recupera a pessoa do banco de dados
        form = ContatoModel2Form(request.POST, instance=pessoa) # cria o formulário com os dados da pessoa
        if form.is_valid(): # valida o formulário
            pessoa = form.save() # salva o formulário na pessoa
            pessoa.save()   # salva a pessoa no banco de dados
            return HttpResponseRedirect(reverse_lazy('contatos:lista-contatos')) # redireciona para a lista de contatos
        else:
            contexto = {
                'form': form,
                'titulo_janela': 'Atualização de Contato',
                'titulo_pagina': 'Atualiza Contato',
                'botao': 'Atualizar',
                'mensagem': 'Erro ao atualizar o contato!'
            }
            return render(request, 'contatos/formContato.html', contexto)

class ContatoCreateView(View):
    '''
    Classe para criar um novo contato
    '''
    def get(self, request, *args, **kwargs):
        '''
        Exibe o formulário de cadastro
        '''
        contexto = {
            'form': ContatoModel2Form, 
            'titulo_janela': 'Cadastro de Contato',
            'titulo_pagina': 'Novo Contato',
            'botao': 'Salvar novo contato',}
        return render(request, 'contatos/formContato.html', contexto)

    def post(self, request, *args, **kwargs):
        '''
        Processa o formulário de cadastro
        '''
        form = ContatoModel2Form(request.POST) # obtem o formulário preenchido
        if form.is_valid(): # valida o formulário
            form.save() # salva o formulário no banco de dados
            contexto = {'form': ContatoModel2Form, 'mensagem': 'Contato salvo com sucesso!'}
            return HttpResponseRedirect(reverse_lazy('contatos:lista')) # redireciona para a lista de contatos
        else:
            contexto = {
                'form': form, 
                'titulo_janela': 'Cadastro de Contato',
                'titulo_pagina': 'Novo Contato',
                'botao': 'Salvar novo contato',
                'mensagem': 'Erro ao salvar o contato!'
            }
            return render(request, 'contatos/formContato.html', contexto)

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
