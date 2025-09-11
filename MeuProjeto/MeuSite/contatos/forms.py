from django import forms
from contatos.models import Pessoa

class ContatoModel2Form(forms.ModelForm):
    dtNasc = forms.DateField(input_formats=['%d/%m/%Y'],)
    class Meta:
        model = Pessoa
        fields = '__all__'