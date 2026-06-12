from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy

from contatos.forms import ContatoModel2Form
from contatos.models import Pessoa

class ContatoListView(ListView):
    model = Pessoa
    template_name = 'contatos-v2/lista-contatos.html'
    context_object_name = 'pessoas'


class ContatoCreateView(CreateView):
    model = Pessoa
    form_class = ContatoModel2Form
    template_name = 'contatos-v2/cria-contato.html'
    success_url = reverse_lazy('contatos-v2:listar-contatos')

class ContatoUpdateView(UpdateView):
    model = Pessoa
    form_class = ContatoModel2Form
    template_name = 'contatos-v2/atualiza-contato.html'
    success_url = reverse_lazy('contatos-v2:listar-contatos')

class ContatoDeleteView(DeleteView):
    model = Pessoa
    template_name = 'contatos-v2/apaga-contato.html'
    success_url = reverse_lazy('contatos-v2:listar-contatos')