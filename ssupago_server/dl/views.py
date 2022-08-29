from django.shortcuts import render


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def post_api(request):
    if request.data :
        # 모델 Import & 예측 요청
        
        return Response("You're looking at question",status=status.HTTP_200_OK)
    else :
        return Response('Error', status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_api(request):
    return Response('GET!!!', status = status.HTTP_200_OK)
    
