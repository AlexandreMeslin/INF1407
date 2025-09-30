from django.shortcuts import render
from .forms import ExemploForm

def home(request):
    return render(request, 'MeuSite/home.html')

def forms(request):
    return render(request, 'MeuSite/forms.html', {'form': ExemploForm()})
