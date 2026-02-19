# Site completo

## Para executar (4 terminais)

### Terminal 1

Utilizado para enviar comandos via console.

Abrir na raiz do repositório

### Terminal 2

Abrir onde estiver o arquivo `requirements.txt`.

```bash
$ source venv/bin/activate
$ cd MeuSite/
$ python manage.py runserver
```

### Terminal 3

Abrir onde estiver o arquivo `tsconfig.json`.

```bash
$ tsc -w
```

### Terminal 4

Abrir onde estiver o arquivo `index.html`.

```bash
$ python -m http.server 8080
```