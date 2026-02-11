from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.edit import UpdateView

def home(request):
    return render(request, 'MeuSite/index.html')

def homeSec(request):
    return render(request, 'seguranca/homeSec.html')

def registro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('sec-home')
    else:
        formulario = UserCreationForm()
    contexto = {'form': formulario}
    return render(request, 'seguranca/registro.html', contexto)

def testaAcesso(user):
    '''
    Função de teste de acesso para verificar se o usuário tem permissão de alterar pessoas.
    A definição dessa função deve preceder a definição da view que a utiliza.

    :param user: O usuário autenticado que está tentando acessar a página secreta.
    :return: True se o usuário tiver permissão de alterar pessoas, False caso contrário.
    '''
    if user.has_perm('contatos.change_pessoa'):
        return True
    else:
        return False

@login_required
@user_passes_test(testaAcesso)
def paginaSecreta(request):
    return render(request, 'seguranca/paginaSecreta.html')

def logout(request):
    return render(request, 'seguranca/logout.html')

class MeuUpdateView(UpdateView):
    def get(self, request, pk, *args, **kwargs):
        if request.user.id == pk:
            return super().get(request, pk, *args, **kwargs)
        else:
            return redirect('sec-home')
