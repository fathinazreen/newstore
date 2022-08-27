from rest_framework import serializers
from mobapi.models import Mobiles

class MobileSerializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField()
    brand=serializers.CharField()
    band=serializers.CharField()
    display=serializers.CharField()
    price=serializers.IntegerField()
    rating=serializers.FloatField()

class MobileModelSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Mobiles
        fields="__all__"
#         field=["name","band","display","price","rating")



