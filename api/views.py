from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class MyView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"helloooowww"})

class GoodMorningView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"GoodMorning"})

class GoodEveningView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"GoodEvening"})

class GoodAfternoonView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"GoodAfternoon"})

class GoodNightView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"GoodNight"})

class AddView(APIView):
    def post(self,request,*args,**kwargs):
        n1=int(request.data.get("num1"))
        n2=int(request.data.get("num2"))
        res=n1+n2
        return Response({"msg":res})

class SubView(APIView):
    def post(self,request,*args,**kwargs):
        n1=int(request.data.get("num1"))
        n2=int(request.data.get("num2"))
        res=n1-n2
        return Response({"res":res})

class MulView(APIView):
    def post(self,request,*args,**kwargs):
        n1=int(request.data.get("num1"))
        n2=int(request.data.get("num2"))
        res=n1*n2
        return Response({"msg":res})

class CubeView(APIView):
    def post(self,request,*args,**kwargs):
        n1=int(request.data.get("num1"))
        res=n1*n1*n1
        return Response({"msg":res})

class FactView(APIView):
    def post(self,request,*args,**kwargs):
        n1=int(request.data.get("num1"))
        fact=1
        for i in range(1,n1+1):
            fact=fact*i
        return Response({"msg":fact})







