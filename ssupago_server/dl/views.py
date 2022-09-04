from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ai_model import model_run
import logging
logger = logging.getLogger(__name__)

@api_view(['POST'])
def post_api(request):
    if request.data :
        # 모델 Import & 예측 요청
        sentence =request.data.get('sentence')
        result = model_run.predict(sentence)
        return Response(result,status=status.HTTP_200_OK)
    else :
        logger.warning('no requested data')
        return Response('Error', status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_api(request):
    return Response('GET!!!', status = status.HTTP_200_OK)
    
