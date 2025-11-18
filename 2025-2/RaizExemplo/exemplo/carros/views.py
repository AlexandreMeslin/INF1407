from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from carros.models import MTCars
from carros.serializers import MTCarsSerializer
from rest_framework import status
# imports para o Swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.

class CarView(APIView):
    @swagger_auto_schema(
        operation_summary="Adiciona um carro",
        operation_description=
            '''
            Adiciona um carro ao banco de dados MTCars.
            É necessário fornecer o nome, mpg, cyl, disp, hp, drat, wt, qsec, vs, am, gear e carb.
            ''',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(
                    type=openapi.TYPE_STRING, 
                    description='Nome do carro',
                    default='NovoCarro',
                ),
                'mpg': openapi.Schema(
                    type=openapi.TYPE_NUMBER, 
                    description='Milhas por galão',
                    default=20.0,
                ),
                'cyl': openapi.Schema(
                    type=openapi.TYPE_INTEGER, 
                    description='Número de cilindros',
                    default=4,
                ),
                'disp': openapi.Schema(
                    type=openapi.TYPE_NUMBER, 
                    description='Deslocamento',
                    default=150.0,
                ),
                'hp': openapi.Schema(
                    type=openapi.TYPE_INTEGER, 
                    description='Cavalos de potência',
                    default=100,
                ),
                #'drat': openapi.Schema(type=openapi.TYPE_NUMBER, description='Taxa de diferencial traseiro'),
                'wt': openapi.Schema(
                    type=openapi.TYPE_NUMBER, 
                    description='Peso do carro',
                    default=2.5,
                ),
                'qsec': openapi.Schema(
                    type=openapi.TYPE_NUMBER, 
                    description='Tempo de quarto de milha',
                    default=18.0,
                ),
                'vs': openapi.Schema(
                    type=openapi.TYPE_INTEGER, 
                    description='Configuração do motor (0 = V/S 1 = Straight)',
                    default=1,
                ),
                'am': openapi.Schema(
                    type=openapi.TYPE_INTEGER, 
                    description='Tipo de transmissão (0 = Automático / 1 = Manual)',
                    default=1,
                ),
                'gear': openapi.Schema(
                    type=openapi.TYPE_INTEGER, 
                    description='Número de marchas',
                    default=4,
                ),
                #'carb': openapi.Schema(type=openapi.TYPE_INTEGER, description='Número de carburadores'),
            },
        ),
        responses={
            201: MTCarsSerializer,
            400: 'Bad Request',
        },
    )
    def post(self, request):
        serializer = MTCarsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, 
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )

class CarsView(APIView):
    @swagger_auto_schema(
        operation_summary="Lista todos os carros",
        operation_description=
            '''
            Retorna a lista de carros do banco de dados MTCars.
            Esta lista é retornada em ordem alfabética 
            pelo nome do carro.
            ''',
        request_body=None,
        responses={
            200: MTCarsSerializer,
        },
        
    )
    def get(self, request):
        # name: nome Python
        # NAME: nome no banco de dados
        carros = MTCars.objects.all().order_by('name')
        # carros: queryset do Django
        # many=True: vários objetos
        serializer = MTCarsSerializer(carros, many=True)
        # Retornando a resposta
        return Response(
            serializer.data, 
            status=status.HTTP_200_OK
        )
