from django import forms

class ExemploForm(forms.Form):
    campoBooleanField = forms.BooleanField(
        required=True,
        label_suffix='*:',
        label='Campo BooleanField', 
        help_text='Marque esta caixa se você concorda.',
        initial=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'classe-booleanfield', 
            }
        )
    )

    campoCharField = forms.CharField(
        required=True,
        label_suffix='*:',
        label='Campo CharField', 
        max_length=100,
        help_text='Digite um texto de até 100 caracteres.',
        initial='Texto inicial',
        widget=forms.TextInput(
            attrs={
                'class': 'classe-charfield', 
                'placeholder': 'Digite algo aqui'
            }
        )
    )

    campoPassword = forms.CharField(
        required=True,
        label_suffix='*:',
        label='Campo Password', 
        max_length=50,
        help_text='Digite sua senha.',
        widget=forms.PasswordInput(
            attrs={
                'class': 'classe-password', 
                'placeholder': 'Senha',
            }
        )
    )

    campoTelefone = forms.CharField(
        required=True,
        label_suffix='*:',
        label='Campo Telefone', 
        max_length=15,
        help_text='Digite um número de telefone no formato (XXX) XXXX-XXXX.',
        initial='(11) 91234-5678',
        widget=forms.TextInput(
            attrs={
                'class': 'classe-telefone', 
                'placeholder': '(XX) XXXXX-XXXX',
                'pattern': r'\(\d{3}\) \d{3,4}-\d{4}'  # Validação simples via HTML5
            }
        )
    )   

    campoChoiceField = forms.ChoiceField(
        required=True,
        label_suffix='*:',
        label='Campo ChoiceField', 
        choices=[
            ('opcao1', 'Opção 1'),
            ('opcao2', 'Opção 2'),
            ('opcao3', 'Opção 3'),
            ('opcao4', 'Opção 4'),
            ('opcao5', 'Opção 5'),
        ],
        help_text='Escolha uma das opções disponíveis.',
        initial='opcao3',   # opção 3 previamente selecionada
        widget=forms.Select(
            attrs={
                'class': 'classe-choicefield',
            }
        )
    )

    campoDateField = forms.DateField(
        required=True,
        label_suffix='*:',
        label='Campo DateField', 
        help_text='Selecione uma data.',
        initial='2024-10-01',
        input_formats=['%d/%m/%Y'],  # Formatos aceitos para entrada de datas
        widget=forms.DateInput(
            attrs={
                'class': 'classe-datefield',
                'type': 'date'  # Usa o seletor de data do HTML5
            }
        )
    )

    campoDateTimeField = forms.DateTimeField(
        required=True,
        label_suffix='*:',
        label='Campo DateTimeField', 
        help_text='Selecione uma data e hora.',
        initial='2024-01-01T12:00',
        input_formats=['%d/%m/%Y %H:%M'],  # Formatos aceitos para entrada de data e hora
        widget=forms.DateTimeInput(
            attrs={
                'class': 'classe-datetimefield',
                'type': 'datetime-local'  # Usa o seletor de data e hora do HTML5
            }
        )
    )

    campoDecimalField = forms.DecimalField(
        required=True,
        label_suffix='*:',
        label='Campo DecimalField', 
        max_digits=10,
        decimal_places=2,
        help_text='Digite um número decimal (máximo 10 dígitos, 2 casas decimais).',
        initial='1234.56',
        widget=forms.NumberInput(
            attrs={
                'class': 'classe-decimalfield', 
                'step': '0.01',  # Permite duas casas decimais
                'placeholder': '0.00'
            }
        )
    )

    campoIntegerField = forms.IntegerField(
        required=True,
        label_suffix='*:',
        label='Campo IntegerField', 
        help_text='Digite um número inteiro.',
        initial=42,
        widget=forms.NumberInput(
            attrs={
                'class': 'classe-integerfield', 
                'placeholder': '0'
            }
        )
    )

    campoGenericIPAddressField = forms.GenericIPAddressField(
        required=True,
        label_suffix='*:',
        label='Campo GenericIPAddressField', 
        protocol='both',  # Aceita tanto IPv4 quanto IPv6
        help_text='Digite um endereço IP (IPv4 ou IPv6).',
        initial='192.168.0.1',
        widget=forms.TextInput(
            attrs={
                'class': 'classe-genericipaddressfield',
                'placeholder': '192.168.10.1'
            }
        )
    )

    campoMultipleChoiceField = forms.MultipleChoiceField(
        required=True,
        label_suffix='*:',
        label='Campo MultipleChoiceField', 
        choices=[
            ('opcao1', 'Opção 1'),
            ('opcao2', 'Opção 2'),
            ('opcao3', 'Opção 3'),
            ('opcao4', 'Opção 4'),
            ('opcao5', 'Opção 5'),
        ],
        help_text='Escolha uma ou mais opções disponíveis.',
        initial=['opcao2', 'opcao4'],  # opções 2 e 4 previamente selecionadas
        widget=forms.Select(
            attrs={
                'class': 'classe-multiplechoicefield',
                'multiple': 'multiple',  # Permite múltiplas seleções
            }
        )
    )

    campoCor = forms.CharField(
        required=True,
        label_suffix='*:',
        label='Campo Cor', 
        help_text='Selecione uma cor.',
        initial='#ff0000',
        widget=forms.TextInput(
            attrs={
                'class': 'classe-cor',
                'type': 'color'  # Usa o seletor de cor do HTML5
            }
        )
    )
    