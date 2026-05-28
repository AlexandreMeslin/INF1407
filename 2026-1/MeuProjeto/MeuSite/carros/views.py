#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from carros.models import MTCars
from carros.serializers import MTCarsSerializer

# Create your views here.

# ------------------------------------
# Detalhes de um carro específico
# ------------------------------------
class CarView(APIView):
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

    def get(self, request, pk):
        '''
        Retorna os detalhes de um carro específico com base no ID fornecido.
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


    def get(self, request):
        '''
        Retorna a lista de carros em formato JSON.
        '''
        cars = MTCars.objects.all().order_by('name')
        serializer = MTCarsSerializer(cars, many=True)
        return Response(serializer.data)
