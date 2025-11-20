from django.shortcuts import render
from rest_framework import status
# Autenticação por token
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import authenticate
from django.contrib.auth import login
# Swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.

class CustomAuthToken(ObtainAuthToken):
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
            200: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'token': openapi.Schema(type=openapi.TYPE_STRING, description='Token de autenticação'),
                },
            ),
            400: 'Bad Request',
        },
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
