from django import forms
from contatos.models import Pessoa
from contatos.models import PessoaComAvatar

class ContatoModel2Form(forms.ModelForm):
    class Meta:
        model = Pessoa
        #fields = ['nome', 'sobrenome', 'email', 'telefone']
        fields = '__all__'
    dtNasc = forms.DateField(
        input_formats=['%d/%m/%Y'],
        label='Data de Nascimento',
        help_text='Formato: DD/MM/AAAA',
        widget=forms.DateInput(attrs={'placeholder': 'DD/MM/AAAA'})
    )

class AvatarForm(forms.ModelForm):
    class Meta:
        model = PessoaComAvatar
        fields = ['avatar']