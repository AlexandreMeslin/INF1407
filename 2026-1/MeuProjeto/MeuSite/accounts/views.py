from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.response import Response

import secrets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from accounts.models import PasswordResetCode
from rest_framework import status
from drf_spectacular.utils import OpenApiExample
from drf_spectacular.utils import OpenApiResponse
from drf_spectacular.utils import extend_schema
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from accounts.serializers import ChangePasswordSerializer
from accounts.serializers import ResetPasswordRequestSerializer
from accounts.serializers import ResetPasswordConfirmSerializer

# Create your views here.

@extend_schema(
    summary="Retorna os dados do usuário autenticado",
    description="Retorna os dados do usuário autenticado, como ID e nome de usuário. Requer autenticação.",
    tags=["accounts"],
    methods=["GET"],
    responses={
      200: OpenApiResponse(description="Dados do usuário retornados com sucesso"),
      401: OpenApiResponse(description="Não autorizado - token JWT ausente ou inválido"),
    },
)
@api_view(['GET'])
@permission_classes([AllowAny])
def whoami(request):
    '''
    Retorna os dados do usuário autenticado.
    '''
    dados = {
        'id': request.user.id,
        'username': request.user.username,
    }

    return Response(dados)

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Alterar senha do usuário autenticado",
        description="Permite que o usuário autenticado altere sua senha fornecendo a senha antiga e a nova senha.",
        tags=["accounts"],
        request=ChangePasswordSerializer,
        responses={
            200: OpenApiResponse(description="Senha alterada com sucesso"),
            400: OpenApiResponse(description="Erro na alteração de senha")
        },
        examples=[
            OpenApiExample(
                "Exemplo de requisição para alterar senha",
                value={
                    "old_password": "S3736-1001!",
                    "new_password": "S12345678!"
                }
            ),
        ],
    )
    def put(self, request):
        '''
        Permite que o usuário autenticado altere sua senha.
        Espera receber a senha antiga em 'old_password' 
        e a nova senha em 'new_password' no corpo da requisição.
        '''
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            user = request.user
            if not user.check_password(serializer.validated_data['old_password']):
                return Response({'error': 'Senha antiga incorreta'}, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({'status': 'Senha alterada com sucesso'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetView(APIView):
    authentication_classes = [] # Desabilita autenticação para esta view
    permission_classes = [AllowAny] # Permite acesso sem autenticação
    
    @extend_schema(
        summary="Solicitar redefinição de senha",
        description="Permite que um usuário solicite um código de redefinição de senha fornecendo seu e-mail.",
        tags=["accounts"],
        request=ResetPasswordRequestSerializer,
        responses={
            200: OpenApiResponse(description="E-mail de redefinição de senha enviado com sucesso"),
            404: OpenApiResponse(description="Nenhum usuário encontrado com este e-mail")
        },
        examples=[
            OpenApiExample(
                "Exemplo de requisição para solicitar redefinição de senha",
                value={ "email": "usuario@exemplo.com" }
            ),
        ],
    )
    def post(self, request):
        '''
        Lida com a solicitação de redefinição de senha.
        Espera receber um e-mail no corpo da requisição para identificar o usuário.
        Gera um token de redefinição de senha e envia um e-mail para o usuário com instruções.
        '''
        serializer = ResetPasswordRequestSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                # A mensagem deveria ser genérica para não revelar se o e-mail existe ou não, 
                # mas para fins de teste e desenvolvimento, vamos retornar um erro específico.
                # Por exemplo: "Se o email existir, enviaremos o código"
                return Response({'message': 'Nenhum usuário encontrado com este e-mail'}, status=status.HTTP_404_NOT_FOUND)
            code = secrets.token_urlsafe(16)
            PasswordResetCode.objects.create(user=user, code=code)

            # send an e-mail to the user
            context = {
                'current_user': user.first_name + ' ' + user.last_name if user.last_name else user.first_name,
                'username': user.username,
                'email': user.email,
                'token': code,
            }

            # render email text
            email_html_message = render_to_string('email/password_reset_email.html', context)
            email_plaintext_message = render_to_string('email/password_reset_email.txt', context)
            msg = EmailMultiAlternatives(
                # title:
                "Redefinição de senha para o site de Exemplos Web",
                # message:
                email_plaintext_message, # ou None para apenas HTML
                # from:
                "noreply@yourdomain.com",
                # to:
                [user.email]
            )
            msg.attach_alternative(email_html_message, "text/html")
            msg.send() 

        return Response({'message': 'E-mail de redefinição de senha enviado com sucesso', 'token': str(code)}, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Confirmar redefinição de senha",
        description="Permite que um usuário confirme a redefinição de senha fornecendo um código de redefinição e a nova senha.",
        tags=["accounts"],
        request=ResetPasswordConfirmSerializer,
        responses={
            200: OpenApiResponse(description="Senha redefinida com sucesso"),
            400: OpenApiResponse(description="Código de redefinição inválido ou expirado")
        },
        examples=[
            OpenApiExample(
                "Exemplo de requisição para confirmar redefinição de senha",
                value={
                    "code": "código-de-redefinição-aqui",
                    "new_password": "S12345678!"
                },
            ),
        ],
    )
    def put(self, request):
        '''
        Lida com a confirmação da redefinição de senha.
        Espera receber um código de redefinição e a nova senha no corpo da requisição.
        Verifica se o código é válido e, se for, redefine a senha do usuário associado.
        '''
        serializer = ResetPasswordConfirmSerializer(data=request.data)
        if serializer.is_valid():
            code = serializer.validated_data['code']
            new_password = serializer.validated_data['new_password']
            try:
                reset_code = PasswordResetCode.objects.get(code=code, used=False)
            except PasswordResetCode.DoesNotExist:
                return Response({'error': 'Código de redefinição inválido ou já utilizado'}, status=status.HTTP_400_BAD_REQUEST)

            if reset_code.is_expired():
                return Response({'error': 'Código de redefinição expirado'}, status=status.HTTP_400_BAD_REQUEST)

            user = reset_code.user
            user.set_password(new_password)
            user.save()
            reset_code.used = True
            reset_code.save()
            return Response({'status': 'Senha redefinida com sucesso'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)