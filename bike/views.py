from django.shortcuts import render

# Create your view
from rest_framework.views import APIView
from rest_framework.response import Response
from bike.models import bikes

class BikeView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"bike":bikes})
    def post(self,request,*args,**kwargs):
        print(request.data)
        qs=request.data
        bikes.append(qs)
        return Response({"msg":request.data})

class BikeDetailView(APIView):
    def get(self,request,*args,**kwargs):
        print("kwargs",kwargs)
        id=kwargs.get("id")
        bik=[bike for bike in bikes if bike.get("id")==id].pop()
        return Response({"data":bik})
