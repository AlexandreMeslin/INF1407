from django.shortcuts import render
from contatos.models import Pessoa
from contatos.models import Endereco
from django.views.generic import View
from contatos.forms import ContatoModel2Form
from django.shortcuts import redirect

# Create your views here.

class ContatoListView(View):
    '''
    Exibe a lista de contatos cadastrados
    '''
    model = Pessoa
    template_name = 'contatos/listaContatos.html'
    context_object_name = 'pessoas'

    def get(self, request, *args, **kwargs):
        '''
        Retorna a lista de contatos
        '''
        pessoas = self.model.objects.all().order_by('nome')
        for pessoa in pessoas:
            print(f'Endereco {pessoa.enderecos.all()}')
        enderecos = Endereco.objects.all()
        context = {'pessoas': pessoas, 'enderecos': enderecos}
        return render(request, self.template_name, context)

class ContatoCreateView(View):
    '''
    Cria um novo contato
    '''
    model = Pessoa
    template_name = 'contatos/criaContato.html'
    form_class = ContatoModel2Form
    success_url = 'contatos:lista-contatos'

    def get(self, request, *args, **kwargs):
        '''
        Exibe o formulário para criação de um novo contato
        '''
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        '''
        Cria um novo contato
        '''
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})  