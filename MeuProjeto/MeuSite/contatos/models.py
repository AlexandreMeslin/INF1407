from django.db import models

# Create your models here.

class Pessoa(models.Model):
    '''
    Modelo que representa uma pessoa no sistema de contatos
    '''
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, help_text="Nome completo")
    idade = models.IntegerField(help_text="Idade em anos")
    salario = models.DecimalField(max_digits=10, decimal_places=2, help_text="Salário mensal em R$")
    email = models.EmailField(unique=True, help_text="Informe um email válido")
    telefone = models.CharField(max_length=17, blank=True, help_text="Telefone com DDD e DDI")
    dtNasc = models.DateField(help_text="Data de nascimento", verbose_name="Data de Nascimento")

    def __str__(self):
        return self.nome + " - " + self.email

class Endereco(models.Model):
    '''
    Modelo que representa um endereço associado a uma pessoa
    '''
    id = models.AutoField(primary_key=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='enderecos')
    logradouro = models.CharField(max_length=200, help_text="Logradouro")
    numero = models.CharField(max_length=10, help_text="Número")
    complemento = models.CharField(max_length=50, blank=True, help_text="Complemento")
    bairro = models.CharField(max_length=100, help_text="Bairro")
    cidade = models.CharField(max_length=100, help_text="Cidade")
    estado = models.CharField(max_length=2, help_text="Estado (UF)")
    cep = models.CharField(max_length=10, help_text="CEP")

    def __str__(self):
        return f"{self.logradouro}, {self.numero} - {self.bairro}, {self.cidade} - {self.estado}, {self.cep}"
