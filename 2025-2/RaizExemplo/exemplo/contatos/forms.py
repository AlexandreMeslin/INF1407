from django import forms
from contatos.models import Pessoa

class ContatoModel2Form(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = "__all__"
