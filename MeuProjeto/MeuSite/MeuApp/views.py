from django.shortcuts import render

# Create your views here.

def home(request):
    '''
    Renderiza a página inicial do MeuApp.

    :param request: Objeto HttpRequest representando a requisição do cliente.
    :return: HttpResponse contendo a página renderizada.
    '''
    return render(request, 'MeuApp/home.html')

def segundaPagina(request):
    '''
    Renderiza a segunda página do MeuApp.

    :param request: Objeto HttpRequest representando a requisição do cliente.
    :return: HttpResponse contendo a página renderizada.
    '''
    return render(request, 'MeuApp/segunda.html')