# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.views import APIView
from rest_framework.permissions import IsAuthenticated
from accounts.serializers import ChangePasswordSerializer
from rest_framework import status

@api_view(['GET'])
def whoiam(request):
    '''
    Retorna os dados do usuário autenticado.
    '''
    dados = {
        'id': request.user.id,
        'username': request.user.username,
    }
    print(f'dados a serem retornados: {dados}')
    return Response(dados)

class CustomAuthToken(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if not user.check_password(serializer.validated_data['old_password']):
                return Response({'error': 'Senha antiga incorreta'}, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({'status': 'Senha alterada com sucesso'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    