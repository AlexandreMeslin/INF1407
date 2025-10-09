# INF1407
Disciplina de Programação para a Web na PUC-Rio

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
![Contributors](https://img.shields.io/github/contributors/AlexandreMeslin/INF1304)
![Open Issues](https://img.shields.io/github/issues/AlexandreMeslin/INF1304)
![Open PRs](https://img.shields.io/github/issues-pr/AlexandreMeslin/INF1304)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

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

## Comandos importantes

```bash
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ django-admin startproject MeuSite
$ python manage.py startapp contatos
$ python manage.py runserver
$ python manage.py makemigrations
$ python manage.py migrate
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