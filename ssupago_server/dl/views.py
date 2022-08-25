from django.shortcuts import render


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# get형식
@api_view(['GET'])
def index(request):
    test_str = 'error'
    if test_str == 'error' :
        return Response('Error', status = status.HTTP_400_BAD_REQUEST)
    return Response("You're looking at question",status=status.HTTP_200_OK)

@api_view(['POST'])
def post_api(request):
    
    if request.data :
        return Response("You're looking at question",status=status.HTTP_200_OK)
    else :
        return Response('Error', status = status.HTTP_400_BAD_REQUEST)
    
# 에러코드, 응답인지 아닌지
