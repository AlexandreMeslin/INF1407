from django.db import models

# Create your models here.

# Novo modelo com avatar
class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    nome = models.CharField(max_length=100, help_text="Nome completo da pessoa")
    idade = models.IntegerField(help_text="Idade da pessoa")
    salario = models.DecimalField(max_digits=8, decimal_places=2, help_text="Salário mensal da pessoa")
    email = models.EmailField(unique=True, help_text="Endereço de email da pessoa", max_length=254)
    telefone = models.CharField(max_length=15, blank=True, help_text="Número de telefone da pessoa (opcional)")
    dtNasc = models.DateField(help_text="Data de nascimento da pessoa", verbose_name="Data de Nascimento")

    class Meta:
        managed = True
        verbose_name = 'Pessoa com Avatar'
        verbose_name_plural = 'Pessoas com Avatar'

    def __str__(self):
        return f'{self.nome} ({self.email})'

    @property
    def iniciais(self):
        if self.nome:
            nomes = self.nome.split()
            primeira_letra = nomes[0][0].upper() if len(nomes[0]) > 0 else '?'
            if len(nomes) > 1:
                segunda_letra = nomes[-1][0].upper() if len(nomes[-1]) > 0 else '?'
            else:
                segunda_letra = nomes[0][1].upper() if len(nomes[0]) > 1 else primeira_letra
            return f'{primeira_letra}{segunda_letra}'
        else:
            return "??"
        