#!/usr/bin/env python

import os
import django
import sys

# Adiciona o diretório 'MeuSite' (pai do settings.py) ao sys.path
# MeuProjeto/MeuSite é o diretório que contém o módulo MeuSite
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # MeuProjeto
meusite_dir = os.path.join(project_dir, 'MeuSite')
sys.path.append(meusite_dir)

# Configurações do Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MeuSite.settings")
django.setup()

# Agora podemos importar os modelos
from contatos.models import Pessoa, Endereco

def main():
    # Criar uma pessoa
    p = Pessoa.objects.create(
        nome="Maria Silva",
        idade=30,
        salario=5000.00,
        email="maria@email.com",
        telefone="(21) 99999-8888",
        dtNasc="1993-05-12"
    )

    # Criar endereços para essa pessoa
    Endereco.objects.create(
        pessoa=p,
        logradouro="Rua das Flores",
        numero="123",
        bairro="Centro",
        cidade="Rio de Janeiro",
        estado="RJ",
        cep="20000-000"
    )

    Endereco.objects.create(
        pessoa=p,
        logradouro="Av. Atlântica",
        numero="456",
        bairro="Copacabana",
        cidade="Rio de Janeiro",
        estado="RJ",
        cep="22000-000"
    )

    # Listar endereços da pessoa
    print("Endereços de", p.nome)
    for e in p.enderecos.all():
        print(e)

if __name__ == "__main__":
    main()