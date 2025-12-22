# INF1407

## Disciplina de Programação para a Web na PUC-Rio.

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
![Contributors](https://img.shields.io/github/contributors/AlexandreMeslin/INF1407)
![Open Issues](https://img.shields.io/github/issues/AlexandreMeslin/INF1407)
![Open PRs](https://img.shields.io/github/issues-pr/AlexandreMeslin/INF1407)
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
![GitHub commits since tagged version](https://img.shields.io/github/commits-since/AlexandreMeslin/INF1407/v2025.2)

![GitHub stars](https://img.shields.io/github/stars/AlexandreMeslin/INF1407?style=social)
![GitHub forks](https://img.shields.io/github/forks/AlexandreMeslin/INF1407?style=social)
![GitHub followers](https://img.shields.io/github/followers/AlexandreMeslin)
![GitHub User's stars](https://img.shields.io/github/stars/AlexandreMeslin)
![GitHub watchers](https://img.shields.io/github/watchers/AlexandreMeslin/INF1407)

**Frameworks & Tools:**

![Django](https://img.shields.io/badge/Django-000000?style=flat-square&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-2D3748?style=flat-square&logo=sqlite&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-FF9900?style=flat-square&logo=amazonaws&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-4169E1?style=flat-square&logo=Javascript&logoColor=white)
![Typescript](https://img.shields.io/badge/TypeScript-4169E1?style=flat-square&logo=Typescript&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-4169E1?style=flat-square&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-4169E1?style=flat-square&logo=css&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05033?style=flat-square&logo=git&logoColor=white)

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
from django.urls.conf import include
from <app> import views

app_name = '<app>'

urlpatterns = [
    path("<path>/", views.<função>, name="<nome>"),
    path("<path>/", include('<app>.urls')),
    path('<path>/', views.ClasseView.as_view(), name='<nome>'),
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

### Para habilitar o auto-complete para o `Django CLI`

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

# Acessando o Container registry

## Autenticação

> Não use o **token** gerado pelo *Codespace* porque o usuário do token é `codespace` e não o seu usuário.

Para criar um **token**, no seu repositório, clique na sua foto, selecione `Settings`, `<> Developer settings`. 
Expanda `Personal access tokens` e clique em `Tokens (classic)`.Clique em `Generate new token` e escolha `Generate new token (classic)`.
No campo `Note`, informe um nome para o seu **token** e marque as opões:

- [x] write:packages
- [x] delete:packages

Clique em `Generate token`.
Copie o **token** gerado e crie uma variável chamada `GITHUB_TOKEN` com esse valor para substituir o **token** original do *Codespace*.

```bash
GITHUB_TOKEN="sakinevasseaviasky?"
```

Faça o login:

```bash
echo $GITHUB_TOKEN | docker login ghcr.io -u USERNAME --password-stdin
```

Saída esperada

```bash
$ echo $GITHUB_TOKEN | docker login ghcr.io -u USER
NAME --password-stdin

WARNING! Your credentials are stored unencrypted in '/home/codespace/.docker/config.json'.
Configure a credential helper to remove this warning. See
https://docs.docker.com/go/credential-store/

Login Succeeded
```
## Construíndo a imagem

```bash
docker build -t ghcr.io/alexandremeslin/prog_web .
```

Saída esperada

```bash
$ docker build -t ghcr.io/alexandremeslin/prog_web .
[+] Building 5.8s (8/8) FINISHED                                                                                             docker:default
 => [internal] load build definition from Dockerfile                                                                                   0.1s
 => => transferring dockerfile: 110B                                                                                                   0.0s
 => [internal] load metadata for docker.io/library/httpd:latest                                                                        0.3s
 => [auth] library/httpd:pull token for registry-1.docker.io                                                                           0.0s
 => [internal] load .dockerignore                                                                                                      0.0s
 => => transferring context: 2B                                                                                                        0.0s
 => [internal] load build context                                                                                                      0.0s
 => => transferring context: 318B                                                                                                      0.0s
 => [1/2] FROM docker.io/library/httpd:latest@sha256:f9b88f3f093d925525ec272bbe28e72967ffe1a40da813fe84df9fcb2fad3f30                  4.7s
 => => resolve docker.io/library/httpd:latest@sha256:f9b88f3f093d925525ec272bbe28e72967ffe1a40da813fe84df9fcb2fad3f30                  0.0s
 => => sha256:4742a9e996d171d036e208e8261ee1a7278c9513f806a96dabcd6cfe66302739 145B / 145B                                             0.1s
 => => sha256:4f4fb700ef54461cfa02571ae0db9a0dc1e0cdb5577484a6d75e68dc38e8acc1 32B / 32B                                               0.1s
 => => sha256:87a14f0839679cdf72421f2a7c5631a7e8a113354285298ce7e318c9ed8134fc 2.00MB / 2.00MB                                         0.2s
 => => sha256:f9b88f3f093d925525ec272bbe28e72967ffe1a40da813fe84df9fcb2fad3f30 10.14kB / 10.14kB                                       0.0s
 => => sha256:1962df175a86aff6eefa4208caff11e4af980523213fdbcb81a93c19c629f5e7 2.09kB / 2.09kB                                         0.0s
 => => sha256:c00bfb4edfeb0206fa0e988e51b588a442deca46cb4ea69b3cd7e08f93b429ae 7.99kB / 7.99kB                                         0.0s
 => => sha256:0e4bc2bd6656e6e004e3c749af70e5650bac2258243eb0949dea51cb8b7863db 29.78MB / 29.78MB                                       1.0s
 => => sha256:9cd0271fa7514efc0ced1e0bcdef82af8591b9006e3468633965deb4fd2085f9 13.43MB / 13.43MB                                       5.4s
 => => sha256:5b4d5959fc7583ac425d94096a05b143ec3547d698d6d202e07f37ee1366db72 291B / 291B                                             0.3s
 => => extracting sha256:0e4bc2bd6656e6e004e3c749af70e5650bac2258243eb0949dea51cb8b7863db                                              1.2s
 => => extracting sha256:4742a9e996d171d036e208e8261ee1a7278c9513f806a96dabcd6cfe66302739                                              0.0s
 => => extracting sha256:4f4fb700ef54461cfa02571ae0db9a0dc1e0cdb5577484a6d75e68dc38e8acc1                                              0.0s
 => => extracting sha256:87a14f0839679cdf72421f2a7c5631a7e8a113354285298ce7e318c9ed8134fc                                              0.2s
 => => extracting sha256:9cd0271fa7514efc0ced1e0bcdef82af8591b9006e3468633965deb4fd2085f9                                              0.4s
 => => extracting sha256:5b4d5959fc7583ac425d94096a05b143ec3547d698d6d202e07f37ee1366db72                                              0.0s
 => [2/2] COPY index.html /usr/local/apache2/htdocs/                                                                                   0.0s
 => exporting to image                                                                                                                 0.6s
 => => exporting layers                                                                                                                0.5s
 => => writing image sha256:ca9ad63fad124a9eb58d2653bb26a0ce82b2ec9659cef302c5b6cb264bcc5761                                           0.0s
 => => naming to ghcr.io/alexandremeslin/prog_web                                                                                      0.0s
```

## Subindo a imagem

```bash
docker push ghcr.io/alexandremeslin/prog_web:latest
```

Saída esperada:

```bash
$ docker push ghcr.io/alexandremeslin/prog_web:latest
The push refers to repository [ghcr.io/alexandremeslin/prog_web]
18f559fb8e35: Pushed 
3ecb2dcd5414: Pushed 
1b73832a4868: Pushed 
5dc0365682c6: Pushed 
5f70bf18a086: Pushed 
de88e4999fda: Pushed 
70a290c5e58b: Pushed 
latest: digest: sha256:79eb996ea9f28ed5f649436e1663ed595c25564ba3532b33fdd858a1eade67de size: 1779
```
