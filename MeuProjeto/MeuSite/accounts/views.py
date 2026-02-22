# Create your views here.
import secrets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from accounts.models import PasswordResetCode
from accounts.serializers import ChangePasswordSerializer
from accounts.serializers import ResetPasswordRequestSerializer
from accounts.serializers import ResetPasswordConfirmSerializer
from rest_framework import status
from drf_spectacular.utils import OpenApiExample
from drf_spectacular.utils import extend_schema
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

@api_view(['GET'])
def whoami(request):
    '''
    Retorna os dados do usuário autenticado.
    '''
    dados = {
        'id': request.user.id,
        'username': request.user.username,
    }
    return Response(dados)

class CustomAuthToken(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Alterar senha do usuário autenticado",
        description="Permite que o usuário autenticado altere sua senha fornecendo a senha antiga e a nova senha.",
        tags=["accounts"],
        request=ChangePasswordSerializer,
        responses={
            200: "Senha alterada com sucesso", 
            400: "Erro na alteração da senha"
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

        Exemplo de sequência de requisições usando curl:

        1. Obter o token de autenticação (substitua USERNAME e PASSWORD):

        $ curl -X POST -H "Content-Type: application/json" -d '{"username": "meslin", "password": "S3736-1001!"}' http://localhost:8000/api/token/ | json_pp
        {
        "access" : "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzcxNTI1MTA2LCJpYXQiOjE3NzE1MjQ4MDYsImp0aSI6ImYxYWM3NjE3N2UxMzQ5ZTg5YzcwYTUxZGY2ZTAzNjFmIiwidXNlcl9pZCI6IjEifQ.RIi6RWh6BcUxcFqOogGbbisy3QyayLD0tWatk0S_LiQ",
        "refresh" : "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3MTYxMTIwNiwiaWF0IjoxNzcxNTI0ODA2LCJqdGkiOiIwMDMyYjk2NDA4ODE0NTk1YmQzYmUwZGY2ZWUzMzY2MyIsInVzZXJfaWQiOiIxIn0.LYjmRY9C9L74qQ-qMx86fn1km6hdSPH27A6GGzU0hAw"
        }

        2. Alterar a senha (substitua YOUR_ACCESS_TOKEN):

        $ curl "http://localhost:8000/accounts/change-password/" -H "Content-Type: application/json" -X PUT -d '{"old_password": "S3736-1001!", "new_password": "S87522578!"}' -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzcxNTI1MTA2LCJpYXQiOjE3NzE1MjQ4MDYsImp0aSI6ImYxYWM3NjE3N2UxMzQ5ZTg5YzcwYTUxZGY2ZTAzNjFmIiwidXNlcl9pZCI6IjEifQ.RIi6RWh6BcUxcFqOogGbbisy3QyayLD0tWatk0S_LiQ"
        {"status":"Senha alterada com sucesso"}

        3. Tentar obter um novo token com a senha antiga (deve falhar):

        $ curl -X POST -H "Content-Type: application/json" -d '{"username": "meslin", "password": "S3736-1001!"}' http://localhost:8000/api/token/ | json_pp
        {
        "detail" : "Usuário e/ou senha incorreto(s)"
        }

        4. Obter um novo token com a nova senha (deve funcionar):

        $ curl -X POST -H "Content-Type: application/json" -d '{"username": "meslin", "password": "S87522578!"}' http://localhost:8000/api/token/ | json_pp
        {
        "access" : "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzcxNTI1MTU1LCJpYXQiOjE3NzE1MjQ4NTUsImp0aSI6IjFmZjI5MjU1MWVmZDQyZGJhZDBjMDU0MjQ5ODlmNTEzIiwidXNlcl9pZCI6IjEifQ.YNFCwQakLh69pXv4XkvDrODODc08gWUXglDTdIojJIU",
        "refresh" : "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3MTYxMTI1NSwiaWF0IjoxNzcxNTI0ODU1LCJqdGkiOiI0YTlkY2Y4ZTgwNzA0OTQ1YTQzYjdjZDhlOTNlNDQ3OCIsInVzZXJfaWQiOiIxIn0.RrFpwNfGLeMKVQEKsHWiol0XxejHCbWTTiIv9o9EpYc"
        }
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
    '''
    View para lidar com requisições de redefinição de senha.
    Permite que um usuário solicite um código de redefinição de senha 
    e, em seguida, use esse código para definir uma nova senha.
    '''
    permission_classes = [] # Permite acesso sem autenticação

    @extend_schema(
        summary="Solicitar redefinição de senha",
        description='''
            Permite que um usuário solicite um código de redefinição de senha fornecendo seu e-mail. 
            O sistema enviará um e-mail com um código de redefinição se o e-mail estiver associado a uma conta.
            ''',
        tags=["accounts"],
        request=ResetPasswordRequestSerializer,
        responses={
            200: "E-mail de redefinição de senha enviado com sucesso", 
            404: "Nenhum usuário encontrado com este e-mail"
        },
        examples=[
            OpenApiExample(
                "Exemplo de requisição para solicitar redefinição de senha",
                value={
                    "email": "usuario@exemplo.com"
                }
            )
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
            
            # Cria código de redefinição de senha e salva no banco de dados
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
                email_plaintext_message,	 # ou None para apenas HTML
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
        description='''
            Permite que um usuário confirme a redefinição de senha usando um código de redefinição e uma nova senha. 
            O sistema verificará se o código é válido e, se for, redefinirá a senha do usuário.
            ''',
        tags=["accounts"],
        request=ResetPasswordConfirmSerializer,
        responses={
            200: "Senha redefinida com sucesso", 
            400: "Código expirado ou inválido",
            404: "Código de redefinição não encontrado",
        },
        examples=[
            OpenApiExample(
            "Exemplo de requisição para confirmar redefinição de senha",
            value={
                "code": "código_de_redefinição_recebido_no_email",
                "new_password": "S12345678!",
                }
            ),
        ],
    )
    def put(self, request):
        '''
        Lida com a confirmação da redefinição de senha.
        Espera receber um código de redefinição e a nova senha no corpo da requisição.
        Verifica se o código é válido e, se for, redefine a senha do usuário.
        '''
        print(f'Requisição recebida para confirmar redefinição de senha: {request.data}')
        serializer = ResetPasswordConfirmSerializer(data=request.data)
        if serializer.is_valid():
            code = serializer.validated_data['code']
            new_password = serializer.validated_data['new_password']

            try:
                reset_code = PasswordResetCode.objects.get(code=code, used=False)
                if reset_code.is_expired():
                    return Response({'error': 'Código expirado'}, status=status.HTTP_400_BAD_REQUEST)
                user = reset_code.user
                user.set_password(new_password)
                user.save()
                reset_code.used = True
                reset_code.save()
            except PasswordResetCode.DoesNotExist:
                return Response({'error': 'Código inválido'}, status=status.HTTP_404_NOT_FOUND)
            return Response({'message': 'Senha redefinida com sucesso'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



    '''
    *** Não funcionou porque o token foi quebrado e foi inserido caracteres = no final de cada linha do token. O token deve ser enviado sem quebras de linha. ***
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'O campo de e-mail é obrigatório'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'Nenhum usuário encontrado com este e-mail'}, status=status.HTTP_404_NOT_FOUND)
        
        token = AccessToken.for_user(user)

        # DEBUG
        print(f'Token gerado para o usuário {user.username} ({user.email}): "{token}"')

        # send an e-mail to the user
        context = {
            'current_user': user.first_name + ' ' + user.last_name if user.last_name else user.first_name,
            'username': user.username,
            'email': user.email,
            'token': token,
        }

        # render email text
        email_html_message = render_to_string('email/password_reset_email.html', context)
        email_plaintext_message = render_to_string('email/password_reset_email.txt', context)
        msg = EmailMultiAlternatives(
            # title:
            "Redefinição de senha para o site de Exemplos Web",
            # message:
            email_plaintext_message,	 # ou None para apenas HTML
            # from:
            "noreply@yourdomain.com",
            # to:
            [user.email]
        )
        msg.attach_alternative(email_html_message, "text/html")
        msg.send() 

        return Response({'message': 'E-mail de redefinição de senha enviado com sucesso', 'token': str(token)}, status=status.HTTP_200_OK)

    def put(self, request):
        token = request.data.get('token')
        new_password = request.data.get('new_password')

        print(f'Token recebido: {token}')
        print(f'Nova senha recebida: {new_password}')

        if not token or not new_password:

            print(f'Campos obrigatórios ausentes: token={token}, new_password={new_password}')

            return Response({'error': 'Os campos de token e nova senha são obrigatórios'}, status=status.HTTP_400_BAD_REQUEST)
        
        print(f'Validando token: {token}')

        try:
            access_token = AccessToken(token)
            user_id = access_token['user_id']
            user = User.objects.get(id=user_id)
            user.set_password(new_password)
            user.save()
            return Response({'message': 'Senha redefinida com sucesso'}, status=status.HTTP_200_OK)
        except Exception as e:

            print(f'Erro ao redefinir senha: {e}')

            return Response({'error': 'Token inválido ou expirado'}, status=status.HTTP_400_BAD_REQUEST)
    '''
