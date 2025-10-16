from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import renderer_classes
from rest_framework.renderers import JSONRenderer

# Create your views here.

class ExemploClasse(APIView):
    def get(self, request):
        return Response(
            {
                "mensagem": "Olá, mundo!",
                "msg": "mensagem via método GET"
            },
            status=status.HTTP_200_OK
        )

    def post(self, request):
        return Response(
            {
                "mensagem": "Olá, mundo!",
                "msg": "mensagem via método POST"
            },
            status=status.HTTP_200_OK
        )

    def put(self, request):
        return Response(
            {
                "mensagem": "Olá, mundo!",
                "msg": "mensagem via método PUT"
            },
            status=status.HTTP_200_OK
        )

    def delete(self, request):
        return Response(
            {
                "mensagem": "Olá, mundo!",
                "msg": "mensagem via método DELETE"
            },
            status=status.HTTP_200_OK
        )

@api_view(('GET',)) # aqui tem que terminar por vírgula
@renderer_classes((JSONRenderer,))  # ✅ CORRETO
def exemploGet(request):
    respostaJSON = {
        "mensagem": "Olá, mundo!",
        "msg": "mensagem via método GET de função"
    }
    return Response(
        respostaJSON,
        status=status.HTTP_200_OK
    )

@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def exemploPost(request):
    return Response(
        {
            "mensagem": "Olá, mundo!",
            "msg": "mensagem via método POST de função"
        },
        status=status.HTTP_200_OK
    )

@api_view(('PUT', 'DELETE'))    # aqui não precisa terminar por vírgula
@renderer_classes((JSONRenderer,))
def exemploPutDelete(request):
    return Response(
        {
            "mensagem": "Olá, mundo!",
            "msg": "mensagem via método PUT ou DELETE de função"
        },
        status=status.HTTP_200_OK
    )
