'''
Created on 2023-10-15

@seealso https://docs.djangoproject.com/en/5.2/ref/forms/fields/#built-in-field-classes
'''
from django import forms
from django.forms.widgets import DateInput
from django.forms.widgets import SelectDateWidget

'''
Exemplo de formulário com vários tipos de campos.
'''
class ExemploForm(forms.Form):
    campoBooleano = forms.BooleanField( 
        required=True, 
        label="Campo booleano", 
        label_suffix=": ", 
        initial=True, 
        help_text="Marque ou desmarque", 
        error_messages = {
            'required': 'Esse campo booleano é necessário',
            'invalid': "Campo booleano inválido",
        },
        disabled=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'classeBooleano',
        }),
    )

    campoTexto = forms.CharField( 
        required=True, 
        label="Campo texto", 
        label_suffix=": ", 
        initial="Exemplo de campo texto", 
        help_text="Entre um texto", 
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo texto inválido",
        },
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'classeTexto',
        }),
    )

    campoBusca = forms.CharField( 
        required=True, 
        label="Campo busca", 
        label_suffix=": ", 
        initial="Exemplo de campo busca", 
        help_text="Entre uma busca", 
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo busca inválido",
        },
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'classeBusca',
            'type': 'search',
        }),
    )

    campoTelefone = forms.CharField( 
        required=True, 
        label="Campo telefone", 
        label_suffix=": ", 
        initial="555-123-1234", 
        help_text="Entre um telefone", 
        error_messages = {
            'required': 'Esse campo é necessário',
            'invalid': "Campo telefone inválido",
        },
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'classeTelefone',
            'type': 'tel',
            'pattern': "[0-9]{3}-[0-9]{3}-[0-9]{4}",
        }),
    )

    campoSenha = forms.CharField( 
        required=True, 
        label="Campo senha", 
        label_suffix=": ", 
        initial="Exemplo de campo senha", 
        help_text="Entre uma senha", 
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo senha inválido",
        },
        max_length=100,
        widget=forms.PasswordInput(attrs={
            'class': 'classeSenha',
        })
    )

    campoArea = forms.CharField( 
        required=True, 
        label="Campo área", 
        label_suffix=": ", 
        initial= 
            "Exemplo de campo área.\n" +
            "O texto pode ter várias linhas.",
        help_text="Entre um texto com várias linhas", 
        error_messages = {
            'required': 'Esse campo área é necessário',
            'invalid': "Campo área inválido",
        },
        max_length=100,
        widget=forms.Textarea(attrs={
            'class': 'classeArea',
            'cols': 40, 'rows': 10,
        }),
    )

    campoCor = forms.CharField( 
        required=True, 
        label='Campo cor',
        label_suffix=": ", 
        initial='#FF0000',
        help_text='Escolha uma cor',
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo cor inválido",
        },
        widget=forms.TextInput(attrs={
            'class': 'classeCor', 
        'type': 'color'}),
  	)

    campoRadio = forms.ChoiceField( 
        required=True, 
        label="Campo rádio", 
        label_suffix=": ", 
        initial="opcao2", 
        help_text="Escolha uma opção", 
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo rádio inválido",
        },
        choices=[
            ('opcao1','opcao 1'),('opcao2','opcao 2'),
            ('opcao3','opcao 3'),('opcao4','opcao 4'),
        ],
        widget=forms.RadioSelect(attrs={
            'class': 'classeRadio',
        }),
    )

    campoSelect = forms.ChoiceField( 
        required=True, 
        label="Campo select", 
        label_suffix=": ", 
        initial="opcao3", 
        help_text="Escolha uma opção", 
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo select inválido",
        },
        choices=[
            ('opcao1','opcao 1'),('opcao2','opcao 2'),
            ('opcao3','opcao 3'),('opcao4','opcao 4'),
        ],
        widget=forms.Select(attrs={
            'class': 'classeSelect'
        }),
    )

    campoSelectMultiplo = forms.ChoiceField( 
        required=True, 
        label="Campo select multiplo", 
        label_suffix=": ", 
        initial=["opcao2","opcao3"], 
        help_text="Escolha várias opções", 
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo inválido",
        },
        choices=[
            ('opcao1','opcao 1'),('opcao2','opcao 2'),
            ('opcao3','opcao 3'),('opcao4','opcao 4'),
        ],
        widget=forms.Select(attrs={
            'class': 'classeSelect',
            'multiple': 'multiple',
        }),
    )

    campoCheckbox = forms.ChoiceField( 
        required=True, 
        label="Campo checkbox", 
        label_suffix=": ", 
        initial=["opcao1","opcao3"], 
        help_text="Escolha uma opção", 
        error_messages = {
            'required': 'Esse campo checkbox é necessário',
            'invalid': "Campo checkbox inválido",
        },
        choices=[
            ('opcao1','opcao 1'),('opcao2','opcao 2'),
            ('opcao3','opcao 3'),('opcao4','opcao 4'),
        ],
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'classeSelectMultiplo',
        }),
    )

    campoData = forms.DateField(
        required=True, 
        label="Campo data", 
        label_suffix=": ", 
        initial="2023-10-15", 
        help_text="Entre uma data", 
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo data inválido",
        },
        disabled=False,
        widget=SelectDateWidget(
            years=range(1980, 2031), 
            attrs={
                'class': 'classeData',
            }
        ),
    )
    
    campoDataPicker = forms.DateField(
        required=True,  
        label="Campo data picker",
        label_suffix=": ", 
        initial='1970-01-02',
        help_text="Entre uma data", 
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo inválido",
        },
        disabled=False,
        widget=DateInput(attrs={
            'class': 'classeDataPicker',
            'type': 'date',
        },), 
    )

    campoDateTimeField = forms.DateTimeField(
        required=True, 
        label="Campo data e hora", 
        label_suffix=": ", 
        initial="2023-10-15 14:30:00", 
        help_text="Entre uma data e hora", 
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo data e hora inválido",
        },
        disabled=False,
        widget=forms.DateTimeInput(attrs={
            'class': 'classeDataHora',
            'type': 'datetime-local',
        },),
    )

    campoDecimal = forms.DecimalField( 
        required=True, 
        label="Campo decimal", 
        label_suffix=": ", 
        initial="87.52", 
        help_text="Entre um número real", 
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo decimal inválido",
        },
        disabled=False,
        widget=forms.NumberInput(attrs={
            'class': 'classeNumeroReal',
            'min': '-15', 'max': '100', 'step': '0.2',
        }),
        max_digits=5,
        decimal_places=3,
    )

    campoDurationField = forms.DurationField(
        required=True, 
        label="Campo duração", 
        label_suffix=": ", 
        initial="12:30:15", 
        help_text="Entre uma duração (hh:mm:ss)", 
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo duração inválido",
        },
        disabled=False,
        widget=forms.TextInput(attrs={
            'class': 'classeDuracao',
            'type': 'time',
            'pattern': "[0-9]{2}:[0-9]{2}:[0-9]{2}",
        }),
    )

    campoEmail = forms.EmailField( 
        required=True, 
        label="Campo email", 
        label_suffix=": ", 
        initial="Exemplo de campo email", 
        help_text="Entre um endereço de email", 
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo email inválido",
        },
        disabled=False,
        max_length=100,
        widget=forms.EmailInput(attrs={
            'class': 'classeEmail',
        },)
    )

    campoArquivo = forms.FileField( 
        required=True, 
        label="Campo arquivo", 
        label_suffix=": ", 
        initial="Exemplo de campo arquivo", 
        help_text="Selecione um arquivo", 
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo arquivo inválido",
        },
        disabled=False,
        max_length=100,
        widget=forms.ClearableFileInput(attrs={
            'class': 'classeArquivo',
            'multiple': False,
        }),
    )

    campoFilePathField = forms.FilePathField( 
        required=True, 
        label="Campo file path", 
        label_suffix=": ", 
        initial="/var/log/syslog", 
        help_text="Selecione um arquivo do sistema", 
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo file path inválido",
        },
        disabled=False,
        path="/var/log",
        match=".*\.log$",
        recursive=True,
        widget=forms.Select(attrs={
            'class': 'classeFilePath',
        }),
    )

    campoFloatField = forms.FloatField( 
        required=True, 
        label="Campo float", 
        label_suffix=": ", 
        initial="87.52", 
        help_text="Entre um número real", 
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo float inválido",
        },
        disabled=False,
        widget=forms.NumberInput(attrs={
            'class': 'classeFloat',
            'min': '-15', 'max': '100', 'step': '0.2',
        }),
    )

    campoGenericIPAddressField = forms.GenericIPAddressField( 
        required=True, 
        label="Campo IP", 
        label_suffix=": ", 
        initial="192.168.0.1",
        protocol='both',    # 'both', 'IPv4' or 'IPv6'
        help_text="Entre um endereço IP", 
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo IP inválido",
        },
        disabled=False,
        widget=forms.TextInput(attrs={
            'class': 'classeIP',
        }),
    )

    campoImageField = forms.ImageField( 
        required=True, 
        label="Campo imagem", 
        label_suffix=": ", 
        initial="Exemplo de campo imagem", 
        help_text="Selecione uma imagem", 
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo imagem inválido",
        },
        disabled=False,
        max_length=100,
        widget=forms.ClearableFileInput(attrs={
            'class': 'classeImagem',
            'multiple': False,
        }),
    )

    campoInteiro = forms.IntegerField( 
        required=True, 
        label="Campo número", 
        label_suffix=": ", 
        initial="8752", 
        help_text="Entre um número inteiro", 
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo inteiro inválido",
        },
        disabled=False,
        widget=forms.NumberInput(attrs={
            'class': 'classeNumero',
            'min': '-15', 'max': '100', 'step': '10',
        }),
    )

    campoFaixa = forms.IntegerField( 
        required=True, 
        label="Campo faixa", 
        label_suffix=": ", 
        initial="8752", 
        help_text="Selecione um valor", 
        error_messages = {
            'required': 'Esse campo faixa é necessário',
            'invalid': "Campo faixa inválido",
        },
        disabled=False,
        widget=forms.NumberInput(attrs={
            'class': 'classeFaixa',
            'type': 'range',
            'min': '-15', 'max': '100', 'step': '10',
        }),
    )

    campoJSONField = forms.JSONField( 
        required=True, 
        label="Campo JSON", 
        label_suffix=": ", 
        initial='{"nome": "João", "idade": 30}', 
        help_text="Entre um texto JSON", 
        error_messages = {
            'required': 'Esse campo JSON é necessário',
            'invalid': "Campo JSON inválido",
        },
        disabled=False,
        widget=forms.Textarea(attrs={
            'class': 'classeJSON',
            'cols': 40, 'rows': 10,
        }),
    )

    campoMultipleChoiceField = forms.MultipleChoiceField( 
        required=True, 
        label="Campo múltipla escolha", 
        label_suffix=": ", 
        initial=["opcao2", "opcao3"],
        help_text="Escolha várias opções", 
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo múltipla escolha inválido",
        },
        choices=[
            ('opcao1','opcao 1'),('opcao2','opcao 2'),
            ('opcao3','opcao 3'),('opcao4','opcao 4'),
        ],
        widget=forms.SelectMultiple(attrs={
            'class': 'classeMultiplaEscolha',
        }),
    )

    campoNullBooleanField = forms.NullBooleanField( 
        required=False, 
        label="Campo booleano nulo", 
        label_suffix=": ", 
        initial=None, 
        help_text="Marque, desmarque ou deixe em branco", 
        error_messages = {
            'invalid': "Campo booleano nulo inválido",
        },
        disabled=False,
        widget=forms.NullBooleanSelect(attrs={
            'class': 'classeBooleanoNulo',
        }),
    )

    campoRegexField = forms.RegexField( 
        required=True, 
        label="Campo regex", 
        label_suffix=": ", 
        initial="abc123", 
        help_text="Entre um texto que combine com a expressão regular [a-zA-Z]{3}[0-9]{3}", 
        error_messages = {
            'required': 'Esse campo regex é necessário',
            'invalid': "Campo regex inválido",
        },
        regex=r'^[a-zA-Z]{3}[0-9]{3}$',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'classeRegex',
        }),
    )

    campoSlugField = forms.SlugField( 
        required=True, 
        label="Campo slug", 
        label_suffix=": ", 
        initial="exemplo-de-campo-slug", 
        help_text="Entre um texto slug (apenas letras, números, hífens ou underscores)", 
        error_messages = {
            'required': 'Esse campo slug é necessário',
            'invalid': "Campo slug inválido",
        },
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'classeSlug',
        }),
    )

    campoTimeField = forms.TimeField(
        required=True, 
        label="Campo hora", 
        label_suffix=": ", 
        initial="14:30:00", 
        help_text="Entre uma hora (hh:mm:ss)", 
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo hora inválido",
        },
        disabled=False,
        widget=forms.TimeInput(attrs={
            'class': 'classeHora',
            'type': 'time',
            'pattern': "[0-9]{2}:[0-9]{2}:[0-9]{2}",
        }),
    )

    campoTypeChoiceField = forms.TypedChoiceField( 
        required=True, 
        label="Campo escolha tipada", 
        label_suffix=": ", 
        initial="2", 
        help_text="Escolha uma opção", 
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo escolha tipada inválido",
        },
        choices=[
            ('1','opcao 1'),('2','opcao 2'),
            ('3','opcao 3'),('4','opcao 4'),
        ],
        coerce=int,
        widget=forms.Select(attrs={
            'class': 'classeEscolhaTipada',
        }),
    )

    campoTypedMultipleChoiceField = forms.TypedMultipleChoiceField( 
        required=True, 
        label="Campo múltipla escolha tipada", 
        label_suffix=": ", 
        initial=["2","3"], 
        help_text="Escolha várias opções", 
        error_messages = {
            'required': 'Campo necessário',
            'invalid': "Campo múltipla escolha tipada inválido",
        },
        choices=[
            ('1','opcao 1'),('2','opcao 2'),
            ('3','opcao 3'),('4','opcao 4'),
        ],
        coerce=int,
        widget=forms.SelectMultiple(attrs={
            'class': 'classeMultiplaEscolhaTipada',
        }),
    )

    campoURL = forms.URLField( 
        required=True, 
        label="Campo URL", 
        label_suffix=": ", 
        initial="Exemplo de campo URL", 
        help_text="Entre uma URL", 
        error_messages = {
            'required': 'Esse campo URL é necessário',
            'invalid': "Campo URL inválido",
        },
        disabled=False,
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'classeURL',
        }),
    )

    campoUUIDField = forms.UUIDField( 
        required=True, 
        label="Campo UUID", 
        label_suffix=": ", 
        initial="12345678-1234-5678-1234-567812345678", 
        help_text="Entre um UUID", 
        error_messages = {
            'required': 'Esse campo UUID é necessário',
            'invalid': "Campo UUID inválido",
        },
        disabled=False,
        widget=forms.TextInput(attrs={
            'class': 'classeUUID',
        }),
    )

    class Meta:
        fields = '__all__'
