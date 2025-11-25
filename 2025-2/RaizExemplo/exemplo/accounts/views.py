#from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth import login
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.

class CustomAuthToken(ObtainAuthToken):
    @swagger_auto_schema(
        operation_summary="Obter username pelo Token",
        operation_description='''
            Endpoint para obter o username associado a um token de autenticação.
            Forneça o token no cabeçalho Authorization para receber o nome de usuário.
            Retorna 200 OK com o nome de usuário em caso de sucesso ou 404 Not Found se o token for inválido.
        ''',
        security=[{'Token': []}],
        manual_parameters=[
            openapi.Parameter(
                'Authorization',
                openapi.IN_HEADER,
                description="Token de autenticação no formato: Token <seu_token_aqui>",
                type=openapi.TYPE_STRING,
                required=True,
                default='Token ',
            ),
        ],
        responses={
            status.HTTP_200_OK: "Nome de usuário obtido com sucesso",
            status.HTTP_404_NOT_FOUND: "Token inválido",
        },
    )
    def get(self, request, *args, **kwargs):
        '''
        Endpoint que recebe um token e retorna o username
        '''
        token_key = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]
        try:
            token = Token.objects.get(key=token_key)
            user = token.user
            return Response({'username': user.username}, status=status.HTTP_200_OK)
        except (Token.DoesNotExist, AttributeError):
            return Response({'username': 'visitante'}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_summary="Obter Token de Autenticação",
        operation_description='''
            Endpoint para autenticar um usuário e obter um token de autenticação.
            Forneça o nome de usuário e a senha para receber um token.
            Retorna 200 OK com o token em caso de sucesso ou 401 Unauthorized em caso de falha.
        ''',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
            },
            required=['username', 'password'],
        ),
        responses={
            status.HTTP_200_OK: "Token gerado com sucesso",
            status.HTTP_401_UNAUTHORIZED: "Credenciais inválidas",
        },
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            login(request, user)
            return Response({
                'token': token.key,
            }, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
