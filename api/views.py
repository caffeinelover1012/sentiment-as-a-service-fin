from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from .sentiment import sentimentAnalysis

@api_view(['GET'])
def returnUser(request):
    usr = {'n':''}
    if hasattr(request.user,"first_name"):
        usr['n'] = request.user.first_name
    else:
        usr['n']="Guest"
    return Response(usr)

@api_view(['GET','POST'])
def senttxt(request):
    text=request.data.get('text')
    # option=request.data.get('model')
    analysis = sentimentAnalysis(text)
    response = {"text":text, "analysis":analysis}
    return Response(response)
