from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from mobile.models import mobiles

class MobilesView(APIView):
    # to get whole details or the mentioned dispkay mobiles details
    def get(self,request,*args,**kwargs):
        # print(request.query_params)
        all_mobiles=mobiles
        if "display" in request.query_params:
          disp=request.query_params.get("display")
          all_mobiles=[mob for mob in all_mobiles if mob.get("display")==disp]
        if "brand" in request.query_params:
          bname=request.query_params.get("brand")
          all_mobiles=[mob for mob in all_mobiles if mob.get("brand")==bname]
        return Response({"mobiles":all_mobiles})

    # to add new data
    def post(self,request,*args,**kwargs):
        print(request.data)
        qs=request.data
        mobiles.append(qs)
        return Response({"msg":request.data})
# to take a particular mobile detail mentioned through url
class MobileDetailView(APIView):
    def get(self,request,*args,**kwargs):
        print("kwargs",kwargs)
        id=kwargs.get("id")
        mob=[mobile for mobile in mobiles if mobile.get("id")==id].pop()
        return Response({"data":mob})
    # to update a particular mobile detail
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        data=request.data
        instance=[mobile for mobile in mobiles if mobile.get("id")==id].pop()
        instance.update(data)
        return Response({"data":instance})
    # to delete a specific mobile detail
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        instance=[mobile for mobile in mobiles if mobile.get("id")==id].pop()
        mobiles.remove(instance)
        return Response({"deleted":instance})

