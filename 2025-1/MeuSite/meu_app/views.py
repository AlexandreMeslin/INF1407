import pyotp
import qrcode
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import TwoFactor
from django.shortcuts import redirect


# Gera QR Code
@login_required
def setup_2fa(request):
    ''' Gera o QR Code para configuração do 2FA. '''
    # Se o usuário ainda não tiver um objeto TwoFactor, criamos um para ele.
    obj, _ = TwoFactor.objects.get_or_create(user=request.user)

    # Geramos o URI para o QR Code usando a biblioteca pyotp.
    totp = pyotp.TOTP(obj.secret)
    # O nome do usuário e o nome do site aparecerão no app de autenticação (Google Authenticator, Authy, etc).
    uri = totp.provisioning_uri(
        name=request.user.username,
        issuer_name="MeuSite-Demo"
    )

    # Geramos o QR Code usando a biblioteca qrcode e retornamos como resposta.
    # O usuário pode escanear esse QR Code com um app de autenticação para configurar o 2FA.
    # O código gerado pelo app de autenticação será verificado na view verify_2fa.
    # Note que o segredo (obj.secret) é armazenado no banco de dados e é usado para verificar os códigos gerados pelo app de autenticação.
    # O segredo deve ser mantido em sigilo, pois quem tiver acesso a ele pode gerar códigos válidos para o 2FA do usuário.
    # Neste exemplo, estamos usando um modelo simples para armazenar o segredo e o status do 2FA, mas em uma aplicação real você pode querer usar uma solução mais robusta e segura.
    # Além disso, este exemplo é apenas para fins educacionais e não deve ser usado em produção sem as devidas considerações de segurança.
    # Aparentemente a biblioteca django-two-factor-auth atualmente não é compatível com django 6, então implementamos uma solução caseira usando pyotp e qrcode para demonstrar o conceito de 2FA.
    img = qrcode.make(uri)
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response


@login_required
def verify_2fa(request):
    ''' Verifica o código 2FA digitado pelo usuário. '''
    obj = TwoFactor.objects.get(user=request.user)
    message = ""

    if request.method == "POST":
        code = request.POST.get("code")
        totp = pyotp.TOTP(obj.secret)

        if totp.verify(code, valid_window=1):
            obj.enabled = True
            obj.save()
            message = "2FA ativado com sucesso!"
        else:
            message = "Código inválido."

    return render(request, "meu_app/verify_2fa.html", {"msg": message})


def require_2fa(view_func):
    '''
    Decorator que exige que o usuário tenha passado pela verificação 2FA.
    Para simplificar, usamos a sessão para marcar que o usuário passou pela verificação.
    '''
    def wrapper(request, *args, **kwargs):
        if not request.session.get("2fa_ok"):
            return redirect("/2fa/verify/")
        return view_func(request, *args, **kwargs)
    return wrapper

@require_2fa
def dashboard(request):
    ''' Exemplo de view protegida por 2FA. '''
    return render(request, "meu_app/dashboard.html")

def home(request):
    '''
    Página inicial pública.
    Apresenta links para todas as páginas do site, incluindo as protegidas por 2FA.
    '''
    return render(request, "meu_app/home.html")