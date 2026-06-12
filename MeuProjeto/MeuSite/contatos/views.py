from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy

from contatos.models import Pessoa
from contatos.forms import ContatoModel2Form

# ----------------------------------------------------
# Classe para listar todos os contatos
# ----------------------------------------------------
class ContatoListView(View):
    def get(self, request, *args, **kwargs):
        '''
        Renderiza a lista de contatos.
        :param request: Objeto HttpRequest representando a requisição do cliente.
        :return: HttpResponse contendo a página renderizada com a lista de contatos.'''
        pessoas = Pessoa.objects.all()
        contexto = { 'pessoas': pessoas, }
        return render(request, 'contatos/lista-contatos.html', contexto)

# ----------------------------------------------------
# Classe para criar um novo contato
# ----------------------------------------------------
class ContatoCreateView(View):
    def get(self, request):
        '''
        Renderiza o formulário para criar um novo contato.
        Este método apresenta o formulário em branco para o usuário preencher os dados do novo contato.

        :param request: Objeto HttpRequest representando a requisição do cliente.
        :return: HttpResponse contendo a página renderizada com o formulário de criação de contato.
        '''
        contexto = {'formulario': ContatoModel2Form()}
        return render(request, 'contatos/cria-contato.html', contexto)

    def post(self, request):
        '''
        Processa os dados enviados pelo formulário para criar um novo contato.
        Este método recebe os dados do formulário, valida-os e, se forem válidos, salva o novo contato no banco de dados.
        Caso os dados sejam inválidos, o formulário é re-renderizado com os erros para que o usuário possa corrigir.

        :param request: Objeto HttpRequest representando a requisição do cliente.
        :return: HttpResponseRedirect para a lista de contatos se o formulário for válido, ou HttpResponse contendo a página renderizada com o formulário e os erros se o formulário for inválido.
        '''
        formulario = ContatoModel2Form(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect(reverse_lazy('contatos:listar-contatos'))
        else:
            contexto = {'formulario': formulario}
            return render(request, 'contatos/cria-contato.html', contexto)

# ----------------------------------------------------
# Classe para atualizar um contato existente
# ----------------------------------------------------
class ContatoUpdateView(View):
    def get(self, request, pk, *args, **kwargs):
        '''
        Renderiza o formulário para atualizar um contato existente.
        Este método busca o contato pelo seu ID (pk) e apresenta um formulário pré-preenchido com os dados atuais do contato para que o usuário possa editá-los.

        :param request: Objeto HttpRequest representando a requisição do cliente.
        :param pk: ID do contato a ser atualizado.
        :return: HttpResponse contendo a página renderizada com o formulário de atualização de contato.
        '''
        pessoa = Pessoa.objects.get(pk=pk)
        formulario = ContatoModel2Form(instance=pessoa)
        contexto = {'pessoa': formulario, }
        return render(request, 'contatos/atualiza-contato.html', contexto)
    
    def post(self, request, pk, *args, **kwargs):
        '''
        Processa os dados enviados pelo formulário para atualizar um contato existente.
        Este método recebe os dados do formulário, valida-os e, se forem válidos, atualiza o contato no banco de dados.
        Caso os dados sejam inválidos, o formulário é re-renderizado com os erros para que o usuário possa corrigir.

        :param request: Objeto HttpRequest representando a requisição do cliente.
        :param pk: ID do contato a ser atualizado.
        :return: HttpResponseRedirect para a lista de contatos se o formulário for válido, ou HttpResponse contendo a página renderizada com o formulário e os erros se o formulário for inválido.
        '''
        pessoa = get_object_or_404(Pessoa, pk=pk)
        formulario = ContatoModel2Form(request.POST, instance=pessoa)
        if formulario.is_valid():
            formulario.save() # cria uma pessoa com os dados do formulário
            return HttpResponseRedirect(reverse_lazy("contatos:lista-contatos"))
        else:
            contexto = {'pessoa': formulario, }
            return render(request, 'contatos/atualiza-contato.html', contexto)

# ----------------------------------------------------
# Classe para apagar um contato existente
# ----------------------------------------------------
class ContatoDeleteView(View):
    def get(self, request, pk, *args, **kwargs):
        '''
        Renderiza a página de confirmação para apagar um contato existente.
        Este método busca o contato pelo seu ID (pk) e apresenta uma página de confirmação para que o usuário possa confirmar a exclusão do contato.

        :param request: Objeto HttpRequest representando a requisição do cliente.
        :param pk: ID do contato a ser apagado.
        :return: HttpResponse contendo a página renderizada com a confirmação de exclusão do contato
        '''
        pessoa = Pessoa.objects.get(pk=pk)
        contexto = { 'pessoa': pessoa, }
        return render(request, 'contatos/apaga-contato.html', contexto)

    def post(self, request, pk, *args, **kwargs):
        '''
        Processa a solicitação de exclusão de um contato existente.
        Este método busca o contato pelo seu ID (pk) e o exclui do banco de dados.

        :param request: Objeto HttpRequest representando a requisição do cliente.
        :param pk: ID do contato a ser apagado.
        :return: HttpResponseRedirect para a lista de contatos após a exclusão.
        '''
        pessoa = Pessoa.objects.get(pk=pk)
        pessoa.delete()
        return HttpResponseRedirect(reverse_lazy("contatos:listar-contatos"))
