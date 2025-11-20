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

    @swagger_auto_schema(
        operation_summary='Dados de um carro',
        operation_description="Obter informações sobre um carro específico",
        responses={
            200: MTCarsSerializer(),
            400: 'Mensagem de erro',
        },
        manual_parameters=[
            openapi.Parameter('id_arg',openapi.IN_PATH,
                default=5,
                type=openapi.TYPE_INTEGER,
                required=True,
                description='id do carro na URL',
            ),
        ],
    )
    def get(self, request, id_arg):
        '''
        Retorna um carro específico pelo ID.
        Se o carro não existir, retorna erro 404.
        Lembrar que o id_arg vem da URL e tem que ter o mesmo nome.
        '''
        carro = self.singleCar(id_arg)
        if carro:
            serializer = MTCarsSerializer(carro)
            return Response(
                serializer.data, 
                status=status.HTTP_200_OK
            )
        else:
            # o id na msg de erro dever ser apenas para depuração
            return Response(
                {'msg': f'Carro com id {id_arg} não encontrado.'}, 
                status=status.HTTP_404_NOT_FOUND
            )

    @swagger_auto_schema(
        operation_summary='Atualiza carro', operation_description="Atualizar um carro existente",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(default='Honda HRV 2021', description='Modelo do carro', type=openapi.TYPE_STRING,),
                'mpg': openapi.Schema(default=24.85, description='Milhas por galão', type=openapi.TYPE_NUMBER,),
                'cyl': openapi.Schema(default=4, description='Quantidade de cilindros', type=openapi.TYPE_INTEGER),
                'disp': openapi.Schema(default=1.8, description='Volume do motor', type=openapi.TYPE_NUMBER),
                'hp': openapi.Schema(default=140, description='Potência em HP', type=openapi.TYPE_INTEGER),
                'wt': openapi.Schema(default=2.87686, description='Peso em 1000 libras', type=openapi.TYPE_NUMBER),
                'qsec': openapi.Schema(
                    default=11.88, 
                    description='Tempo para percorrer 1/4 milha', 
                    type=openapi.TYPE_NUMBER
                ),
                'vs': openapi.Schema(default=0, description='Motor em V ou em linha (straight) (0=v, 1=s)', type=openapi.TYPE_INTEGER),
                'am': openapi.Schema(default=0, description='Transmissão (0=automática, 1=manual)', type=openapi.TYPE_INTEGER),
                'gear': openapi.Schema(default=7, description='Número de marchas para frente', type=openapi.TYPE_INTEGER),
            },
        ),
        responses={200: MTCarsSerializer(), 400: MTCarsSerializer(), },
        manual_parameters=[
            openapi.Parameter(
                'id_arg',
                openapi.IN_PATH, 
                default=41, 
                type=openapi.TYPE_INTEGER,
                required=True, 
                description='id do carro na URL',
            ),
        ],
    )
    def put(self, request, id_arg):
        '''
        Atualiza um carro específico pelo ID.
        Se o carro não existir, retorna erro 400.
        Lembrar que o id_arg vem da URL e tem que ter o mesmo nome.
        '''
        # preciso obter o carro a ser atualizado para ter o seu id
        carro = self.singleCar(id_arg)
        if carro:
            # insere as informações do carro a ser atualizado
            serializer = MTCarsSerializer(
                carro, 
                data=request.data
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data, 
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    serializer.errors, 
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            # o id na msg de erro dever ser apenas para depuração
            return Response(
                {'msg': f'Carro com id {id_arg} não encontrado.'}, 
                status=status.HTTP_404_NOT_FOUND
            )

    def singleCar(self, id_arg):
        '''
        Retorna um carro específico pelo ID.
        Se o carro não existir, retorna None.
        '''
        try:
            queryset = MTCars.objects.get(id=id_arg)
            return queryset
        except MTCars.DoesNotExist:
            return None

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
