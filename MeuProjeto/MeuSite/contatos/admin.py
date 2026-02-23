from django.contrib import admin

# Register your models here.

from contatos.models import Pessoa
from contatos.models import PessoaComAvatar

admin.site.register(Pessoa)
admin.site.register(PessoaComAvatar)
