from django.shortcuts import redirect, render

# Create your views here.

from django.views.generic.base import View
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.http import HttpRequest
from django.http import HttpResponse

from contatos.models import Pessoa
from contatos.forms import ContatoModel2Form

class ContatoListView(View):
    '''
    View para listar todos os contatos cadastrados no banco de dados e renderiza a página de lista de contatos
    Herda da classe View do Django, que é uma classe base para criar views baseadas em classes (CBVs)
    '''
    def get(self, request: HttpRequest) -> HttpResponse:
        '''
        Recupera todas as pessoas do banco de dados 
        e renderiza a página de lista de contatos
        '''
        pessoas = Pessoa.objects.all()  # Recupera todas as pessoas do banco de dados
        contexto = {
            'pessoas': pessoas,
        }
        return render(request, 'contatos/listaContatos.html', contexto)

class ContatoCreateView(View):
    '''
    View para criar um novo contato
    Herda da classe View do Django, que é uma classe base para criar views baseadas em classes (CBVs)
    '''
    def get(self, request: HttpRequest) -> HttpResponse:
        '''
        Renderiza a página de criação de contato com um formulário vazio
        '''
        contexto = {
            'title_head': 'Cria Contato',
            'title_page': 'Criação de Contato',
            'title_legend': 'Formulário de Cadastro',
            'text_submit': 'Cria contato',
            'pessoa': ContatoModel2Form()
        }
        return render(request, 'contatos/formContato.html', contexto)

    def post(self, request: HttpRequest) -> HttpResponse:
        '''
        Processa os dados enviados pelo formulário de criação de contato, valida e salva o novo contato no banco de dados
        '''
        # Cria um formulário preenchido com os dados enviados pelo usuário
        # Os dados são enviados em duas partes: request.POST para os dados do formulário e request.FILES para os arquivos (como o avatar)
        formulario = ContatoModel2Form(request.POST, request.FILES)    # Cria um formulário preenchido com os dados enviados pelo usuário
        if formulario.is_valid():                       # Verifica se os dados do formulário são válidos
            formulario.save()                           # Salva o novo contato no banco de dados
            return HttpResponseRedirect(reverse_lazy('contatos:lista-contatos'))
        else:
            contexto = {
                'title_head': 'Cria Contato',
                'title_page': 'Criação de Contato',
                'title_legend': 'Formulário de Cadastro',
                'text_submit': 'Cria contato',
                'pessoa': formulario,
            }
            return render(request, 'contatos/formContato.html', contexto)

class ContatoDeleteView(View):
    '''
    View para excluir um contato
    Herda da classe View do Django, que é uma classe base para criar views baseadas em classes (CBVs)
    '''
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        '''
        Exibe a pessoa a ser deletada e renderiza a página de confirmação de exclusão

        :param request: A solicitação HTTP GET enviada pelo usuário para confirmar a exclusão do contato
        :param pk: A chave primária do contato a ser excluído, passada como parte da URL
        :return: Renderiza a página de confirmação de exclusão com os detalhes do contato a ser excluído
        '''
        pessoa = Pessoa.objects.get(pk=pk)              # Recupera a pessoa do banco de dados com a chave primária fornecida
        form = ContatoModel2Form(instance=pessoa) # Cria um formulário preenchido com os dados da pessoa para exibir na página de confirmação de exclusão
        contexto = {    # Prepara o contexto com a pessoa a ser deletada
            'title_head': 'Apaga Contato',
            'title_page': 'Confirmação de Exclusão',
            'title_legend': 'Contato a ser excluído',
            'text_submit': 'Excluir contato',
            'status_form': 'form-desativado', # Adiciona uma classe CSS para estilizar o formulário como desativado, indicando que os dados não podem ser editados
            'pessoa': form,
        }               
        return render(request, 'contatos/formContato.html', contexto)

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        '''
        Processa a solicitação de exclusão de um contato, 
        deleta a pessoa do banco de dados e redireciona para a lista de contatos

        :param request: A solicitação HTTP POST enviada pelo usuário para confirmar a exclusão do contato
        :param pk: A chave primária do contato a ser excluído, passada como parte da URL
        :return: Redireciona para a lista de contatos após a exclusão
        '''
        pessoa = Pessoa.objects.get(pk=pk)              # Recupera a pessoa do banco de dados com a chave primária fornecida
        pessoa.delete()                                 # Deleta a pessoa do banco de dados
        return HttpResponseRedirect(reverse_lazy('contatos:lista-contatos'))

class ContatoUpdateView(View):
    '''
    View para atualizar um contato
    Herda da classe View do Django, que é uma classe base para criar views baseadas em classes (CBVs)
    '''
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        '''
        Exibe o formulário para atualizar um contato

        :param request: A solicitação HTTP GET enviada pelo usuário para acessar a página de atualização do contato
        :param pk: A chave primária do contato a ser atualizado, passada como parte da URL
        :return: Renderiza a página de atualização do contato com um formulário preenchido com os dados atuais do contato
        '''
        pessoa = Pessoa.objects.get(pk=pk)              # Recupera a pessoa do banco de dados com a chave primária fornecida
        formulario = ContatoModel2Form(instance=pessoa) # Cria um formulário preenchido com os dados da pessoa
        contexto = {
            'title_head': 'Atualiza Contato',
            'title_page': 'Atualização de Contato',
            'title_legend': 'Dados do Contato',
            'text_submit': 'Atualizar contato',
            'pessoa': formulario,
        }                   # Prepara o contexto com o formulário
        return render(request, 'contatos/formContato.html', contexto)

    def post(self, request: HttpRequest, pk: int) -> HttpResponse:
        '''
        Processa a solicitação de atualização de um contato, 
        atualiza os dados da pessoa no banco de dados e redireciona para a lista de contatos

        :param request: A solicitação HTTP POST enviada pelo usuário para confirmar a atualização do contato
        :param pk: A chave primária do contato a ser atualizado, passada como parte da URL
        :return: Em caso de sucesso, redireciona para a lista de contatos após a atualização, em caso de falha, renderiza a página de atualização do contato com o formulário preenchido com os dados inválidos
        '''
        pessoa = Pessoa.objects.get(pk=pk)                              # Recupera a pessoa do banco de dados com a chave primária fornecida
        formulario = ContatoModel2Form(request.POST, request.FILES, instance=pessoa)   # Cria um formulário preenchido com os dados enviados pelo usuário e a instância da pessoa
        if formulario.is_valid():                                       # Verifica se os dados do formulário são válidos
            formulario.save()                                           # Salva as alterações no banco de dados
            return HttpResponseRedirect(reverse_lazy('contatos:lista-contatos'))
        else:
            contexto = {
                'title_head': 'Atualiza Contato',
                'title_page': 'Atualização de Contato',
                'title_legend': 'Dados do Contato',
                'text_submit': 'Atualizar contato',
                'pessoa': formulario,
            }                   # Prepara o contexto com o formulário preenchido com os dados inválidos
            return render(request, 'contatos/formContato.html', contexto)



def toggle_theme(request):
    '''
    Alterna entre os temas claro e escuro, 
    armazenando a preferência do usuário na sessão.

    :param request: A solicitação HTTP enviada pelo usuário para alternar o tema
    :return: Redireciona para a página anterior após alternar o tema
    '''
    # Recupera o tema atual da sessão, 
    # se não existir, define como "light" por padrão
    current = request.session.get("theme", "light")
    # Alterna o tema para "dark" se o tema atual for "light", 
    # ou para "light" se o tema atual for "dark"
    request.session["theme"] = "dark" if current == "light" else "light"
    # Redireciona para a página anterior usando o cabeçalho HTTP_REFERER,
    # ou para a página inicial ("/") se o cabeçalho não estiver presente
    return redirect(request.META.get("HTTP_REFERER", "/"))
