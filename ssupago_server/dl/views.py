import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from ai_model import model_run

@api_view(['POST'])
def post_api(request):
    if request.data :
        # 모델 Import & 예측 요청
        sentence ="이런 바보멍청이 같은개"
        result = model_run.predict(sentence)
        return Response("You're looking at question"+result,status=status.HTTP_200_OK)
    else :
        return Response('Error', status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_api(request):
    return Response('GET!!!', status = status.HTTP_200_OK)
    
