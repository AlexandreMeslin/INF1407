#from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from carros.models import MTCars
from carros.serializers import MTCarsSerializer
from rest_framework import status

class CarsView(APIView):
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

    def delete(self, request):
        '''
        Deleta todos os carros do banco de dados
        
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

