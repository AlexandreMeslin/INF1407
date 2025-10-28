# INF1407 - updated
Disciplina de Programação para a Web na PUC-Rio

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
![Contributors](https://img.shields.io/github/contributors/AlexandreMeslin/INF1304)
![Open Issues](https://img.shields.io/github/issues/AlexandreMeslin/INF1304)
![Open PRs](https://img.shields.io/github/issues-pr/AlexandreMeslin/INF1304)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
![GitHub Created At](https://img.shields.io/github/created-at/AlexandreMeslin/INF1407)

![Python](https://img.shields.io/badge/language-Python-yellow.svg)
![HTML](https://img.shields.io/badge/language-HTML-brown.svg)
![JavaScript](https://img.shields.io/badge/language-JavaScript-green.svg)
![TypeScript](https://img.shields.io/badge/language-TypeScript-darkgreen.svg)
![CSS](https://img.shields.io/badge/language-css-blue.svg)
![Top Language](https://img.shields.io/github/languages/top/AlexandreMeslin/INF1407)
![Languages Count](https://img.shields.io/github/languages/count/AlexandreMeslin/INF1407)

![Last Commit](https://img.shields.io/github/last-commit/AlexandreMeslin/INF1407)
![Repo Size](https://img.shields.io/github/repo-size/AlexandreMeslin/INF1407)
![Code Size](https://img.shields.io/github/languages/code-size/AlexandreMeslin/INF1407)

![GitHub stars](https://img.shields.io/github/stars/AlexandreMeslin/INF1407?style=social)
![GitHub forks](https://img.shields.io/github/forks/AlexandreMeslin/INF1407?style=social)
![GitHub followers](https://img.shields.io/github/followers/AlexandreMeslin)
![GitHub User's stars](https://img.shields.io/github/stars/AlexandreMeslin)
![GitHub watchers](https://img.shields.io/github/watchers/AlexandreMeslin/INF1407)

## Comandos importantes

```bash
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ django-admin startproject MeuSite
$ python manage.py createsuperuser
$ python manage.py startapp contatos
$ python manage.py runserver
$ python manage.py makemigrations
$ python manage.py migrate
```

## Outros comandos
```bash
$ python manage.py dumpdata        
$ python manage.py optimizemigration  
$ python manage.py sqlsequencereset
$ python manage.py flush           
$ python manage.py squashmigrations
$ python manage.py check             
$ python manage.py inspectdb       
$ python manage.py sendtestemail      
$ python manage.py compilemessages   
$ python manage.py loaddata        
$ python manage.py shell              
$ python manage.py createcachetable  
$ python manage.py makemessages    
$ python manage.py showmigrations     
$ python manage.py test
$ python manage.py dbshell           
$ python manage.py sqlflush           
$ python manage.py testserver
$ python manage.py diffsettings      
$ python manage.py sqlmigrate
```

## Templates básicos

### urls.py
Obs.: Substitua `<app>`, `<path>`, `<função>` e `<nome>` pelos valores desejados.
```python
from django.urls import path
from <app> import views

app_name = '<app>'

urlpatterns = [
    path("<path>/", views.<função>, name="<nome>"),
] 
```

### views.py
Obs.: Substitua `<NomeDaClasse>`, `<contexto>`, `<dados>`, `<app>` e `<arquivo>` pelos valores desejados.
```python
from django.shortcuts import render
from django.views.generic.base import View

class <NomeDaClasse>(View):
    def get(self, request, *args, **kwargs):
        contexto = { '<contexto>': <dados>, }
        return render(request, '<app>/<arquivo>.html', contexto)

def <nomeDaFunção>(request):
    contexto = { '<contexto>': <dados>, }
    return render(request, '<app>/<arquivo>.html', contexto)
```

### template
Obs.: Substitua `<app>`, `<nome>` e `<arquivo>` pelos valores desejados.
```html
{% load static %}
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Título da Página</title>
    <link rel="stylesheet" href="{% static '<app>/css/<arquivo>.css' %}">
    <script src="{% static '<app>/js/<arquivo>.js' %}"></script>
</head>
<body> 
    <h1>Conteúdo da Página</h1>
    <a href="{% url '<app>:<nome>' %}">Link</a>
</body>
</html>
``` 

## Configurações interessantes

### Para habilitar o auto-complete para o `Django CLI^

1. Baixar o script diretamente do repositório oficial do Django:
    ```bash
    wget https://raw.githubusercontent.com/django/django/main/extras/django_bash_completion -O ~/.django_bash_completion
    ```

1. Tornar o script executável:
    ```bash
    chmod +x ~/.django_bash_completion
    ```

1. Incluir o texto no final do arquivo `~/.bashrc`
    ```bash
    # Django bash completion
    if [ -f ~/.django_bash_completion ]; then
        . ~/.django_bash_completion
    fi
    ```
    > Precisa abrir novamente o terminal para funcionar
