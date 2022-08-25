from django.shortcuts import render
# get형식
def index(request):
    return HttpResponse("You're looking at question")
# 에러코드, 응답인지 아닌지
