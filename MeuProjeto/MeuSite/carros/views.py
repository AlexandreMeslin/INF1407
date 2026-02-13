#from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from carros.models import MTCars
from carros.serializers import MTCarsSerializer

class CarsView(APIView):
    def get(self, request):
        queryset = MTCars.objects.all().order_by('name')
        # importante informar que o queryset 
        # tem muitos objetos, por isso o many=True
        serializer = MTCarsSerializer(queryset, many=True)
        return Response(serializer.data)

