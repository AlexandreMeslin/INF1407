from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def home(request):
    '''
    Renderiza a página inicial.
    '''
    return render(request, 'exemplo/home.html')

def homeSec(request):
    '''
    Renderiza a página inicial de segurança.
    '''
    return render(request, 'seguranca/homeSec.html')

def registro(request):
    '''
    Renderiza a página de registro de usuários.
    '''
    if request.method == 'POST':
        # Aqui você pode adicionar a lógica para processar o formulário de registro
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('sec-home')  # Redireciona para a página inicial de segurança após o registro
    else:
        formulario = UserCreationForm()
    contexto = {'form': formulario, }
    return render(request, 'seguranca/registro.html', contexto)

@login_required
def paginaSecreta(request):
    '''
    Renderiza uma página secreta que requer autenticação.
    O decorador @login_required garante que apenas usuários autenticados 
    possam acessar esta página.
    '''
    return render(request, 'privado/paginaSecreta.html')

def logout(request):
    '''
    Apresenta uma página para o usuário confirmar se realmente deseja sair.
    '''
    return render(request, 'seguranca/logout.html')
