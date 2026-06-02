#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from carros.models import MTCars
from carros.serializers import MTCarsSerializer

# Swagger
from drf_spectacular.utils import OpenApiExample, extend_schema, OpenApiResponse

# Create your views here.

# ------------------------------------
# Detalhes de um carro específico
# ------------------------------------
class CarView(APIView):
    @extend_schema(
        summary="Atualiza os detalhes de um carro específico",
        description='''
        Atualiza os detalhes de um carro específico com base no ID fornecido.
        Retorna status:
        - 200 OK se a atualização for bem-sucedida
        - 400 Bad Request se os dados fornecidos forem inválidos
        - 404 Not Found se o carro com o ID fornecido não for encontrado
        Várias linhas com vários blá-blá-blá 
        para mostrar que a descrição pode ser bem detalhada e ocupar várias linhas.

        Antes de atualizar o carro, consulte a base de dados para obter o ID correto
        usando o método GET para listar todos os carros. 
        O ID do carro a ser atualizado deve ser incluído na URL da requisição PUT.
        Copie o resultado, REMOVA a última vírgula e o id (coloque o ID como parâmetro)
        ''',
        tags=["Carros"],
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
    )
    def put(self, request, pk):
        '''
        Atualiza os detalhes de um carro específico com base no ID fornecido.
        Retorna status:
        - 200 OK se a atualização for bem-sucedida
        - 400 Bad Request se os dados fornecidos forem inválidos
        - 404 Not Found se o carro com o ID fornecido não for encontrado
        '''
        try:
            # tenta buscar o carro
            car = MTCars.objects.get(pk=pk)
        except MTCars.DoesNotExist:
            # se o carro não for encontrado, retorna um erro 404
            return Response({'error': 'Carro não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        # se o carro for encontrado, atualiza os dados com base no corpo da requisição
        serializer = MTCarsSerializer(car, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Detalhes de um carro específico",
        description='''
        Retorna os detalhes de um carro específico com base no ID fornecido.
        Retorna status:
        - 200 OK se o carro for encontrado e os detalhes forem retornados com sucesso
        - 404 Not Found se o carro com o ID fornecido não for encontrado
        Várias linhas com vários blá-blá-blá 
        para mostrar que a descrição pode ser bem detalhada e ocupar várias linhas. 
        ''',
        tags=["Carros"],
        responses={
            200: MTCarsSerializer,
            404: OpenApiResponse(description="Carro não encontrado"),
        },
    )
    def get(self, request, pk):
        '''
        Retorna os detalhes de um carro específico com base no ID fornecido.

        :author: EU!!!
        :param pk: int - ID do carro a ser buscado
        :return: JSON com os detalhes do carro, ou um erro 404 se o carro não for encontrado
        '''
        try:
            # tenta buscar o carro
            car = MTCars.objects.get(pk=pk)
        except MTCars.DoesNotExist:
            # se o carro não for encontrado, retorna um erro 404
            return Response({'error': 'Carro não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        # se o carro for encontrado, serializa os dados e retorna a resposta
        serializer = MTCarsSerializer(car)
        return Response(serializer.data, status=status.HTTP_200_OK)

# -----------------------------------
# Cria um carro
# -----------------------------------
class CarCreateView(APIView):
    @extend_schema(
        summary="Cria um novo carro",
        description="Cria um novo carro a partir dos dados fornecidos no corpo da requisição.",
        tags=["Carros"],
        request=MTCarsSerializer,
        responses={
            201: MTCarsSerializer, 
            400: OpenApiResponse(description="Dados inválidos fornecidos")
        },
        examples=[
            OpenApiExample(
                "Exemplo de criação de carro",
                value={
                    "name": "Honda HRV 2021", "mpg": 24.85, "cyl": 4, "disp": 1.8, "hp": 140,
                    "wt": 2.87686, "qsec": 11.88, "vs": 0, "am": 0, "gear": 7,
                },
                request_only=True, # Este exemplo é apenas para a requisição
            ),
        ]
    )
    def post(self, request):
        '''
        Cria um novo carro a partir dos dados fornecidos no corpo da requisição.
        '''
        serializer = MTCarsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# -----------------------------------
# Lista todos os carros
# -----------------------------------
class CarsView(APIView):
    def delete(self, request):
        '''
        Exclui todos os carros do banco de dados.
        Retorna status:
        - 204 No Content se a exclusão for bem-sucedida
        '''
        id_erro = ''    # armazena os IDs dos carros que não foram encontrados
        erro = False    # flag para indicar se houve algum erro
        # nos dados, o nome do campo NÃO pode ser enviado]
        # apenas os IDs dos carros a serem excluídos
        for id in request.data:
            print(f'[DEBUG] ID recebido para exclusão: {id}')
            carro = MTCars.objects.get(id=id)
            if carro:
                carro.delete()
            else:
                id_erro += f'{id} '
                erro = True
        if erro:
            return Response({'error': f'Carros com IDs {id_erro} não encontrados'}, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)


    @extend_schema(
        summary="Lista todos os carros",
        description="Retorna uma lista de todos os carros disponíveis no banco de dados.",
        tags=["Carros"],
        responses={
            200: MTCarsSerializer(many=True),
            500: OpenApiResponse(description="Erro interno do servidor")
        }
    )   
    def get(self, request):
        '''
        Retorna a lista de carros em formato JSON.
        Esse método é chamado quando o cliente faz uma requisição
        GET para a URL associada a essa view.

        Nenhum parâmetro é necessário para essa requisição, 
        pois ela retorna todos os carros disponíveis 
        no banco de dados.
        '''
        cars = MTCars.objects.all().order_by('name')
        serializer = MTCarsSerializer(cars, many=True)
        return Response(serializer.data)
