from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm

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
