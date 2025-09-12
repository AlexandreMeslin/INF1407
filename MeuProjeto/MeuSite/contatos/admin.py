from django.contrib import admin

# Register your models here.

from contatos.models import Pessoa
from contatos.models import Endereco

admin.site.register(Pessoa)
admin.site.register(Endereco)
