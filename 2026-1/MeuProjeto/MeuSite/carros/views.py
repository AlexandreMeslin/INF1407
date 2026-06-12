from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from carros.models import MTCars
from carros.serializers import MTCarsSerializer

# Para o JWT
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view
from rest_framework_simplejwt.authentication import JWTAuthentication

# Swagger
from drf_spectacular.utils import OpenApiExample
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import OpenApiResponse
from drf_spectacular.utils import inline_serializer
from rest_framework import serializers

# Create your views here.

# ------------------------------------
# Detalhes de um carro específico
# ------------------------------------
class CarView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    auth = [{'bearerAuth': []}] # para o Swagger mostrar que é necessário o token JWT

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
        request=inline_serializer(
            name='CarUpdateInput', # Nome que aparecerá na seção 'Schemas' do Swagger
            fields={
                "name": serializers.CharField(default="Honda HRV 2021", help_text="Modelo do carro"),
                "mpg": serializers.FloatField(default=24.85, help_text="Milhas por galão"),
                "cyl": serializers.IntegerField(default=4, help_text="Quantidade de cilindros"),
                "disp": serializers.FloatField(default=1.8, help_text="Volume do motor"),
                "hp": serializers.IntegerField(default=140, help_text="Potência em HP"),
                "wt": serializers.FloatField(default=2.87686, help_text="Peso em 1000 libras"),
                "qsec": serializers.FloatField(default=11.88, help_text="Tempo 1/4 milha"),
                "vs": serializers.IntegerField(default=0, help_text="Motor V ou linha"),
                "am": serializers.IntegerField(default=0, help_text="Transmissão"),
                "gear": serializers.IntegerField(default=7, help_text="Número de marchas"),
            }
        ),
        responses={
            200: MTCarsSerializer,
            400: OpenApiResponse(description="Dados inválidos fornecidos"),
            404: OpenApiResponse(description="Carro não encontrado"),
        },
        examples=[
            OpenApiExample(
                "Exemplo de requisição para atualizar um carro",
                value={
                    "name": "Honda HRV 2021", "mpg": 24.85, "cyl": 4, "disp": 1.8, "hp": 140,
                    "wt": 2.87686, "qsec": 11.88, "vs": 0, "am": 0, "gear": 7,
                },
                request_only=True, # Este exemplo é apenas para a requisição
            ),
            OpenApiExample(
                "Exemplo de resposta à requisição para atualizar um carro",
                value={
                    "id": 8752, "name": "Honda HRV 2021", "mpg": 24.85, "cyl": 4, "disp": 1.8,
                    "hp": 140, "wt": 2.87686, "qsec": 11.88, "vs": 0, "am": 0, "gear": 7,
                },
                response_only=True, # Este exemplo é apenas para a resposta
            ),
        ],
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
        examples=[
            OpenApiExample(
                "Exemplo de criação de carro",
                value={
                    "name": "Honda HRV 2021", "mpg": 24.85, "cyl": 4, "disp": 1.8, 
                    "hp": 140, "wt": 2.87686, "qsec": 11.88, "vs": 0, "am": 0, "gear": 7,
                },
                response_only=True, # Este exemplo é apenas para a resposta
            ),
        ],
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
                    "name": "Honda HRV 2021", "mpg": 24.85, "cyl": 4, "disp": 1.8,
                    "hp": 140, "wt": 2.87686, "qsec": 11.88, "vs": 0, "am": 0, "gear": 7,
                },
                request_only=True, # Este exemplo é apenas para a requisição
            ),
            OpenApiExample(
                "Exemplo de criação de carro",
                value={
                    "id": 8752, "name": "Honda HRV 2021", "mpg": 24.85, "cyl": 4, "disp": 1.8,
                    "hp": 140, "wt": 2.87686, "qsec": 11.88, "vs": 0, "am": 0, "gear": 7,
                },
                response_only=True, # Este exemplo é apenas para a resposta
            ),
        ],
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
    authentication_classes = []
    permission_classes = [AllowAny]

    @extend_schema(
        summary="Lista todos os carros",
        description="Retorna uma lista de todos os carros disponíveis no banco de dados.",
        tags=["Carros"],
        responses={
            200: MTCarsSerializer(many=True),
            500: OpenApiResponse(description="Erro interno do servidor")
        },
        examples=[
            OpenApiExample(
                name="Exemplo de resposta bem-sucedida",
                value=[
                    {
                        "id": 1, "name": "Mazda RX4", "mpg": 21.0, "cyl": 6, "disp": 160.0,
                        "hp": 110, "wt": 2.620, "qsec": 16.46,"vs": 0, "am": 1, "gear": 4
                    },
                    {
                        "id": 2, "name": "Honda Civic", "mpg": 30.5, "cyl": 4, "disp": 1.8,
                        "hp": 140, "wt": 2.5, "qsec": 15.2, "vs": 1, "am": 1, "gear": 5
                    },
                    {
                        "id": 3, "name": "Ford Mustang", "mpg": 19.8, "cyl": 8, "disp": 5.0,
                        "hp": 450, "wt": 3.8, "qsec": 12.9, "vs": 0, "am": 1, "gear": 6
                    }
                ],
                response_only=True,      # ← Importante: só aparece na resposta
                status_codes=["200"],
                description="Exemplo de lista de carros retornada pela API"
            )
        ]
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

        # DEBUG: Imprime o header de autenticação para verificar se o token JWT está sendo enviado corretamente
        print("=" * 50)
        print("AUTH HEADER:")
        print(request.META.get("HTTP_AUTHORIZATION"))
        print("=" * 50)

        cars = MTCars.objects.all().order_by('name')
        serializer = MTCarsSerializer(cars, many=True)
        return Response(serializer.data)
    
    @extend_schema(
        summary="Exclui carros específicos",
        description='''
        Exclui carros específicos com base nos IDs fornecidos no corpo da requisição.
        Retorna status:
        - 204 No Content se a exclusão for bem-sucedida
        - 404 Not Found se algum dos carros com os IDs fornecidos não for encontrado
        Várias linhas com vários blá-blá-blá 
        para mostrar que a descrição pode ser bem detalhada e ocupar várias linhas.
        ''',
        tags=["Carros"],
    )
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
    summary="Exemplo de view protegida",
    description="Endpoint de teste para verificar autenticação JWT.",
    tags=["Testes"],

    responses={
        200: OpenApiResponse(
            description="Requisição bem-sucedida",
            response={"type": "object", "properties": {"message": {"type": "string"}}}
        ),
        401: OpenApiResponse(
            description="Não autorizado - Token ausente ou inválido"
        ),
    },
    examples=[
        OpenApiExample(
            name="Resposta de Sucesso",
            value={"message": "Esta é uma view protegida. Você está autenticado!"},
            response_only=True,
            status_codes=["200"],
        ),
        OpenApiExample(
            name="Erro de Autenticação",
            value={"detail": "Authentication credentials were not provided."},
            response_only=True,
            status_codes=["401"],
        ),
    ],
)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def exemplo_protegido(request):
  return Response({"message": "Esta é uma view protegida. Você está autenticado!"},
                  status=status.HTTP_200_OK)
