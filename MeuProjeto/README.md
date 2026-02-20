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

---

## Árvore de diretórios e arquivos

```
MeuProjeto
├── MeuSite
│   ├── MeuApp
│   │   ├── admin.py
│   │   ├── models.py
│   │   ├── static
│   │   │   └── MeuApp
│   │   │       ├── css
│   │   │       │   └── estilo.css
│   │   │       ├── fonts
│   │   │       ├── img
│   │   │       │   ├── nohtyp.png
│   │   │       │   ├── puc-rio.png
│   │   │       │   └── python.png
│   │   │       └── script
│   │   │           └── javascript.js
│   │   ├── templates
│   │   │   └── MeuApp
│   │   │       ├── home.html
│   │   │       └── segunda.html
│   │   ├── urls.py
│   │   └── views.py
│   ├── MeuSite
│   │   ├── db_router.py
│   │   ├── settings.py
│   │   ├── static
│   │   │   └── MeuSite
│   │   │       └── css
│   │   │           └── estilo.css
│   │   ├── templates
│   │   │   ├── MeuSite
│   │   │   │   └── index.html
│   │   │   └── seguranca
│   │   │       ├── base.html
│   │   │       ├── homeSec.html
│   │   │       ├── login.html
│   │   │       ├── logout.html
│   │   │       ├── paginaSecreta.html
│   │   │       ├── password_change_done.html
│   │   │       ├── password_change_form.html
│   │   │       ├── password_reset_complete.html
│   │   │       ├── password_reset_confirm.html
│   │   │       ├── password_reset_done.html
│   │   │       ├── password_reset_email.html
│   │   │       ├── password_reset_form.html
│   │   │       ├── password_reset_subject.txt
│   │   │       ├── registro.html
│   │   │       └── user_form.html
│   │   ├── urls.py
│   │   └── views.py
│   ├── accounts
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── templates
│   │   │   └── email
│   │   │       ├── password_reset_email.html
│   │   │       └── password_reset_email.txt
│   │   ├── urls.py
│   │   └── views.py
│   ├── carros
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── contatos
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── static
│   │   │   └── contatos
│   │   │       ├── css
│   │   │       │   └── estilo.css
│   │   │       ├── fonts
│   │   │       ├── img
│   │   │       └── js
│   │   ├── templates
│   │   │   └── contatos
│   │   │       ├── apagaContato.html
│   │   │       ├── atualizaContato.html
│   │   │       ├── criaContato.html
│   │   │       ├── links.html
│   │   │       └── listaContatos.html
│   │   ├── urls.py
│   │   └── views.py
│   ├── db.sqlite3
│   ├── manage.py
│   ├── mtcars copy.sqlite3
│   └── mtcars.sqlite3
├── README.md
├── desktop
│   ├── drop_columns.py
│   ├── drop_tables.py
│   ├── listar.py
│   └── listar_tabela.py
├── frontend
│   ├── public
│   │   ├── cabecalho.html
│   │   ├── css
│   │   │   ├── common.css
│   │   │   ├── estilo.css
│   │   │   └── login.css
│   │   ├── fonts
│   │   ├── img
│   │   │   ├── eye-off.svg
│   │   │   └── eye.svg
│   │   ├── index.html
│   │   ├── insereCarro.html
│   │   ├── javascript
│   │   ├── login.html
│   │   ├── passwordChange.html
│   │   ├── passwordChangeDone.html
│   │   ├── passwordReset.html
│   │   ├── passwordResetDone.html
│   │   └── update.html
│   └── typescript
│       ├── cabecalho.ts
│       ├── common.ts
│       ├── constantes.ts
│       ├── insereCarro.ts
│       ├── login.ts
│       ├── passwordChange.ts
│       ├── passwordChangeDone.ts
│       ├── passwordReset.ts
│       ├── passwordResetDone.ts
│       ├── script.ts
│       ├── tsconfig.json
│       └── update.ts
└── requirements.txt
```