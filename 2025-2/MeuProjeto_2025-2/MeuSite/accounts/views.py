from django.shortcuts import render
from rest_framework import status
# Autenticação por token
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth import login
# Swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.contrib.auth import logout

# Create your views here.

class CustomAuthToken(ObtainAuthToken):
    '''
    View personalizada para autenticação por token.
    Permite que os usuários obtenham um token de autenticação fornecendo nome de usuário e senha.
    '''
    @swagger_auto_schema(
        operation_summary='Obter token de autenticação',
        operation_description="Autentica o usuário e retorna um token de autenticação",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Nome de usuário'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Senha do usuário'),
            },
            required=['username', 'password'],
        ),
        responses={
            status.HTTP_200_OK: 'Token de autenticação retornado com sucesso',
            status.HTTP_400_BAD_REQUEST: 'Requisição inválida - Dados incorretos',
            status.HTTP_401_UNAUTHORIZED: 'Unauthorized - Credenciais inválidas',
        },
    )
    def post(self, request, *args, **kwargs):
        '''
        Autentica o usuário e retorna um token de autenticação
        :param request: Requisição HTTP contendo 'username' e 'password'
        :return: Resposta HTTP com o token de autenticação
        '''
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                login(request, user)
                return Response({'token': token.key})
            else:
                return Response({'error': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary='Obter username do usuário autenticado',
        operation_description="Retorna o nome de usuário do usuário autenticado ou 'visitante' se não autenticado",
        security=[{'Token': []}],   # Indica que o endpoint requer autenticação por token
        manual_parameters=[
            openapi.Parameter(
                'Authorization', 
                openapi.IN_HEADER, 
                description="Token de autenticação do usuário no formato 'Token \<<i>token</i>\>'", 
                type=openapi.TYPE_STRING,
                default='token ',
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description='Username retornado com sucesso',
                schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={'username': openapi.Schema(type=openapi.TYPE_STRING)}),
                examples={
                    'application/json': {
                        'username': 'usuario_exemplo'
                    }
                }
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description='Usuário não autenticado',
                examples={
                    'application/json': {
                        'username': 'visitante'
                    }
                }
            ),
        },
    )
    def get(self, request, *args, **kwargs):
        '''
        :parm request: Requisição HTTP contendo o token de autenticação
        :return: Resposta HTTP com o username ou a palavra 'visitante' se não autenticado
        '''
        try:
            token_key = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]
            token_obj = Token.objects.get(key=token_key)
            user = token_obj.user
            return Response({'username': user.username}, status=status.HTTP_200_OK)
        except (IndexError, Token.DoesNotExist, AttributeError):
            return Response({'username': 'visitante'}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary='Logout do usuário',
        operation_description="Encerra a sessão do usuário removendo o token de autenticação",
        manual_parameters=[
            openapi.Parameter(
                'Authorization', 
                openapi.IN_HEADER, 
                description="Token de autenticação do usuário no formato 'Token \<<i>token</i>\>'", 
                type=openapi.TYPE_STRING,
                default='token ',
            ),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                description='Logout realizado com sucesso',
                examples={
                    'application/json': {
                        'msg': 'Logout realizado com sucesso'
                    }
                }
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description='Requisição inválida - Token inválido ou ausente',
                examples={
                    'application/json': {
                        'msg': 'Token inválido ou ausente'
                    }
                }
            ),
            status.HTTP_401_UNAUTHORIZED: openapi.Response(
                description='Não autorizado - Token inválido',
                examples={
                    'application/json': {
                        'msg': 'Token inválido'
                    }
                }
            ),
            status.HTTP_403_FORBIDDEN: openapi.Response(
                description='Usuário não autenticado',
                examples={
                    'application/json': {
                        'msg': 'Usuário não autenticado'
                    }
                }
            ),
            status.HTTP_404_NOT_FOUND: openapi.Response(
                description='Token não encontrado',
                examples={
                    'application/json': {
                        'msg': 'Token não encontrado'
                    }
                }
            ),
            status.HTTP_500_INTERNAL_SERVER_ERROR: openapi.Response(
                description='Erro interno do servidor',
                examples={
                    'application/json': {
                        'msg': 'Erro interno do servidor'
                    }
                }
            ),
        },
    )
    def delete(self, request, *args, **kwargs):
        '''
        Encerra a sessão do usuário removendo o token de autenticação
        :param request: Requisição HTTP contendo o token de autenticação
        :return: Resposta HTTP confirmando o logout
        '''
        try:
            token_key = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]
            token_obj = Token.objects.get(key=token_key)
        except(Token.DoesNotExist, IndexError, AttributeError):
            return Response({'msg': 'Token inválido ou ausente'}, status=status.HTTP_400_BAD_REQUEST)
        user = token_obj.user
        if user.is_authenticated:
            request.user = user
            logout(request)
            token_obj = Token.objects.get(user=user)
            token_obj.delete()
            return Response({'msg': 'Logout realizado com sucesso'}, status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'Usuário não autenticado'}, status=status.HTTP_403_FORBIDDEN)

    @swagger_auto_schema(
        operation_summary='Trocar senha',
        operation_description="Troca a senha do usuário autenticado, atualiza o token de autenticação em caso de sucesso",
        manual_parameters=[
            openapi.Parameter(
                'Authorization', 
                openapi.IN_HEADER, 
                description="Token de autenticação do usuário no formato 'Token \<<i>token</i>\>'", 
                type=openapi.TYPE_STRING,
                default='token ',
            ),
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'old_password': openapi.Schema(type=openapi.TYPE_STRING, description='Senha antiga do usuário'),
                'new_password1': openapi.Schema(type=openapi.TYPE_STRING, description='Nova senha do usuário'),
                'new_password2': openapi.Schema(type=openapi.TYPE_STRING, description='Confirmação da nova senha do usuário'),
            },
            required=['old_password', 'new_password1', 'new_password2'],
        ),
        responses={
            status.HTTP_200_OK: openapi.Response(
                description='Senha alterada com sucesso',
                examples={
                    'application/json': {
                        'mensagem': 'Senha alterada com sucesso. Por favor, faça login novamente.',
                        'token': 'token'
                    }
                }
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description='Requisição inválida - Dados incorretos',
                examples={
                    'application/json': {
                        'msg': 'As novas senhas não coincidem',
                        'new_password1': ['Senha antiga incorreta.']
                    }
                }
            ),
            status.HTTP_401_UNAUTHORIZED: 'Unauthorized - Credenciais inválidas',
        },
    )
    def put(self, request, *args, **kwargs):
        '''
        Permite a troca de senha do usuário autenticado
        :param request: Requisição HTTP contendo o token de autenticação e a nova senha
        :return: Resposta HTTP confirmando a troca de senha
        '''
        try:
            token_key = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]
            token_obj = Token.objects.get(key=token_key)
        except(Token.DoesNotExist, IndexError, AttributeError):
            return Response({'msg': 'Token inválido ou ausente'}, status=status.HTTP_400_BAD_REQUEST)
        user = token_obj.user
        if user.is_authenticated:
            old_password = request.data.get('old_password')
            new_password = request.data.get('new_password1')
            confirmPassword = request.data.get('new_password2')

            if new_password != confirmPassword:
                return Response({'msg': 'As novas senhas não coincidem'}, status=status.HTTP_400_BAD_REQUEST)
            if user.check_password(old_password):
                user.set_password(new_password)
                user.save()

                try:
                    token_obj = Token.objects.get(user=user)
                    token_obj.delete()
                    token_obj, _ = Token.objects.get_or_create(user=user)
                except Token.DoesNotExist:
                    # nada a fazer se o token não existir
                    pass
                return Response(
                    {
                        'mensagem': 'Senha alterada com sucesso. Por favor, faça login novamente.',
                        'token': token_obj.key
                    }, 
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                        'mensagem': 'Senha antiga incorreta',
                        'old_password': ['Senha antiga incorreta.']
                    }, 
                    status=status.HTTP_400_BAD_REQUEST
                )
