#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from carros.models import MTCars
from carros.serializers import MTCarsSerializer

# Create your views here.

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

class CarsView(APIView):
    def get(self, request):
        '''
        Retorna a lista de carros em formato JSON.
        '''
        cars = MTCars.objects.all().order_by('name')
        serializer = MTCarsSerializer(cars, many=True)
        return Response(serializer.data)
