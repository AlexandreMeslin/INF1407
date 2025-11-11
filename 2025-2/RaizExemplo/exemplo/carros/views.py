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
