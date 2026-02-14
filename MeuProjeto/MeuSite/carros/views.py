#from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from carros.models import MTCars
from carros.serializers import MTCarsSerializer
from rest_framework import status
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import OpenApiExample
from drf_spectacular.utils import OpenApiParameter
from drf_spectacular.utils import OpenApiTypes

class CarsView(APIView):
    @extend_schema(
        summary="Lista todos os carros",
        description="Retorna uma lista de todos os carros em formato JSON, ordenados alfabeticamente por nome.",
        tags=["Carros"],
        responses={
            200: MTCarsSerializer(many=True),
            400: "Bad Request"
        }
    )
    def get(self, request):
        '''
        Lista todos os carros em formato JSON em ordem alfabética
        
        :param self: a própria classe
        :param request: o objeto request (pedido HTTP)
        '''
        queryset = MTCars.objects.all().order_by('name')
        # importante informar que o queryset 
        # tem muitos objetos, por isso o many=True
        serializer = MTCarsSerializer(queryset, many=True)
        return Response(serializer.data)

    @extend_schema(
        summary="Remove carros específicos",
        description="Remove carros do banco de dados com base nos IDs fornecidos no corpo do pedido HTTP.",
        tags=["Carros"],
        request={
            'application/json': {
                'type': 'array',
                'items': {
                    'type': 'integer',
                    'description': 'ID do carro a ser removido',
                    'example': [1, 5, 10],
                }
            },
        },
        responses={
            204: "No Content",
            400: "Bad Request"
        }
    )
    def delete(self, request):
        '''
        Remove carros específicos do banco de dados
        
        :param self: a própria classe
        :param request: o objeto request (pedido HTTP)
        '''
        id_erro = ""    # Lista de ids que não foram deletados
        erro = False    # Flag para indicar se houve erro

        for id in request.data:
            try:
                print(f"🗑️ Tentando deletar carro com ID: {id}")
                car = MTCars.objects.get(pk=id)
                car.delete()
            except MTCars.DoesNotExist:
                id_erro += f"{id} "  # Adiciona o id que causou erro à lista
                erro = True
                print(f"❌ Erro ao deletar carro com ID: {id} - Carro não encontrado")

        if erro:
            return Response(
                {"error": f"Não foi possível deletar os carros com os seguintes IDs: {id_erro}"},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)  # 204 No Content

class CarView(APIView):
    @extend_schema(
        summary="Obtém dados de um carro específico",
        description="Retorna os dados de um carro específico em formato JSON, com base no ID fornecido na URL.",
        tags=["Carros"],
        parameters=[
            OpenApiParameter(
                name="pk",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True,
                description="ID do carro a ser obtido",
                default=5,
            )
        ],
        responses={
            200: MTCarsSerializer,
            404: OpenApiExample(
                'Carro não encontrado',
                value={"error": "Carro com o ID especificado não encontrado."},
                response_only=True,  # Este exemplo é apenas para a resposta
            ),
        },
    )
    def get(self, request, pk):
        '''
        Retorna um carro específico em formato JSON
        
        :param self: a própria classe
        :param request: o objeto request (pedido HTTP)
        :param pk: o ID do carro a ser retornado
        '''
        # 'pk' é o mesmo nome que colocamos em urls.py
        try:
            car = MTCars.objects.get(pk=pk)
        except MTCars.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)  # 404 Not Found

        serializer = MTCarsSerializer(car)
        return Response(serializer.data, status=status.HTTP_200_OK)  # 200 OK
    
    @extend_schema(
        summary="Atualiza um carro específico",
        description="Atualiza os dados de um carro específico no banco de dados com base no ID fornecido na URL e nos dados enviados no corpo do pedido HTTP.",
        tags=["Carros"],
        parameters=[
            OpenApiParameter(
                name="pk",
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
                required=True,
                description="ID do carro a ser atualizado",
                default=5,
            )
        ],
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "default": "Honda HRV 2021", "description": "Modelo do carro"},
                    "mpg": {"type": "number", "default": 24.85, "description": "Milhas por galão"},
                    "cyl": {"type": "integer", "default": 4, "description": "Quantidade de cilindros"},
                    "disp": {"type": "number", "default": 1.8, "description": "Volume do motor"},
                    "hp": {"type": "integer", "default": 140, "description": "Potência em HP"},
                    "wt": {"type": "number", "default": 2.87686, "description": "Peso em 1000 libras"},
                    "qsec": {"type": "number", "default": 11.88, "description": "Tempo 1/4 milha"},
                    "vs": {"type": "integer", "default": 0, "description": "Motor V ou linha"},
                    "am": {"type": "integer", "default": 0, "description": "Transmissão"},
                    "gear": {"type": "integer", "default": 7, "description": "Número de marchas"},
                },
            }
        },
        responses={
            200: MTCarsSerializer,
            400: OpenApiExample(
                'Dados errados',
                value={"erro": "Dados inválidos. Verifique os campos e tente novamente."},
            ),
            404: OpenApiExample(
                'Carro não encontrado',
                value={"error": "Carro com o ID especificado não encontrado."},
                response_only=True,  # Este exemplo é apenas para a resposta
            ),
        },
    )
    def put(self, request, pk):
        '''
        Atualiza um carro específico a partir dos dados enviados no corpo do pedido HTTP
        
        :param self: a própria classe
        :param request: o objeto request (pedido HTTP)
        :param pk: o ID do carro a ser atualizado
        '''
        try:
            car = MTCars.objects.get(pk=pk)
        except MTCars.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)  # 404 Not Found

        serializer = MTCarsSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)  # 200 OK
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # 400 Bad Request

class CarCreateView(APIView):
    @extend_schema(
        summary="Cria um novo carro",
        description="Cria um novo carro no banco de dados a partir dos dados fornecidos no corpo do pedido HTTP.",
        tags=["Carros"],
        request=MTCarsSerializer,
        responses={
            201: MTCarsSerializer,
            400: OpenApiExample(
                'Dados errados',
                value={"erro": "Dados inválidos. Verifique os campos e tente novamente."},
            )
        },
        examples=[
            OpenApiExample(
                "Exemplo de criação de carro",
                value={
                    "name": "Honda HRV 2021",
                    "mpg": 24.85,
                    "cyl": 4,
                    "disp": 1.8,
                    "hp": 140,
                    "wt": 2.87686,
                    "qsec": 11.88,
                    "vs": 0,
                    "am": 0,
                    "gear": 7,
                },
                request_only=True,  # Este exemplo é apenas para a requisição
            )
        ]
    )
    def post(self, request):
        '''
        Insere um carro no banco de dados a partir dos dados enviados no corpo do pedido HTTP
        
        :param self: a própria classe
        :param request: o objeto request (pedido HTTP)
        '''
        serializer = MTCarsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # 201 Created
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # 400 Bad Request
