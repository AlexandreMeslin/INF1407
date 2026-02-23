from django.db import models

# Create your models here.

class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, help_text="Nome completo da pessoa")
    idade = models.IntegerField(help_text="Idade da pessoa")
    salario = models.DecimalField(max_digits=8, decimal_places=2, help_text="Salário mensal da pessoa")
    email = models.EmailField(unique=True, help_text="Endereço de email da pessoa", max_length=254)
    telefone = models.CharField(max_length=15, blank=True, help_text="Número de telefone da pessoa (opcional)")
    dtNasc = models.DateField(help_text="Data de nascimento da pessoa", verbose_name="Data de Nascimento")

    def __str__(self):
        return f'{self.nome} ({self.email})'


# Novo modelo com avatar
class PessoaComAvatar(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    class Meta:
        managed = True
        verbose_name = 'Pessoa com Avatar'
        verbose_name_plural = 'Pessoas com Avatar'

    def __str__(self):
        return f'Avatar de {self.pessoa.nome}'