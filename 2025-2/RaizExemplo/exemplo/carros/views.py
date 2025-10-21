from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from carros.models import MTCars
from carros.serializers import MTCarsSerializer
from rest_framework import status

# Create your views here.

class CarsView(APIView):
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
