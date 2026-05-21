#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from carros.models import MTCars
from carros.serializers import MTCarsSerializer

# Create your views here.

class CarsView(APIView):
    def get(self, request):
        '''
        Retorna a lista de carros em formato JSON.
        '''
        cars = MTCars.objects.all().order_by('name')
        serializer = MTCarsSerializer(cars, many=True)
        return Response(serializer.data)
