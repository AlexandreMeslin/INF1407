# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.views import APIView
from rest_framework.permissions import IsAuthenticated
from accounts.serializers import ChangePasswordSerializer
from rest_framework import status
from drf_spectacular.utils import extend_schema
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

@api_view(['GET'])
def whoiam(request):
    '''
    Retorna os dados do usuário autenticado.
    '''
    dados = {
        'id': request.user.id,
        'username': request.user.username,
    }
    print(f'dados a serem retornados: {dados}')
    return Response(dados)

class CustomAuthToken(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Alterar senha do usuário autenticado",
        description="Permite que o usuário autenticado altere sua senha fornecendo a senha antiga e a nova senha.",
        tags=["Contas", "Autenticação"],
        request=ChangePasswordSerializer,
        responses={
            200: "Senha alterada com sucesso", 
            400: "Erro na alteração da senha"
        },
        examples=[
            {
                "name": "Exemplo de requisição para alterar senha",
                "value": {
                    "old_password": "S3736-1001!",
                    "new_password": "S12345678!"
                }
            },
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
    @extend_schema(
        summary="Solicitar redefinição de senha",
        description="Permite que um usuário solicite a redefinição de sua senha fornecendo seu endereço de e-mail.",
        tags=["Contas", "Autenticação"],
        request=ChangePasswordSerializer,
        responses={
            200: "E-mail de redefinição de senha enviado com sucesso", 
            400: "Erro na solicitação de redefinição de senha"
        },
        examples=[
            {
                "name": "Exemplo de requisição para solicitar redefinição de senha",
                "value": {
                    "email": "usuario@exemplo.com"
                }
            }
        ],
    )
    def post(self, request):
        '''
        Permite que um usuário solicite a redefinição de sua senha fornecendo seu endereço de e-mail.
        '''
        email = request.data.get('email')
        if not email:
            return Response({'error': 'O campo de e-mail é obrigatório'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'Nenhum usuário encontrado com este e-mail'}, status=status.HTTP_404_NOT_FOUND)
        
        token = AccessToken.for_user(user)
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
        '''
        Permite que um usuário redefina sua senha fornecendo um token de acesso válido e a nova senha.
        '''
        token = request.data.get('token')
        new_password = request.data.get('new_password')

        if not token or not new_password:
            return Response({'error': 'Os campos de token e nova senha são obrigatórios'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            access_token = AccessToken(token)
            user_id = access_token['user_id']
            user = User.objects.get(id=user_id)
            user.set_password(new_password)
            user.save()
            return Response({'message': 'Senha redefinida com sucesso'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Token inválido ou expirado'}, status=status.HTTP_400_BAD_REQUEST)
        