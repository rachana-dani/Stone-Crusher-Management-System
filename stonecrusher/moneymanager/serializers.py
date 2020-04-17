from .models import AuthorizedUser,Worker,SaleLog, Resource, StoneType, DieselStock, SaleBill
from rest_framework import serializers


class AuthorizedUserSerailizer(serializers.Serializer):
    class Meta:
        model = AuthorizedUser
        fields = ["username", "password"]

class WorkerSerializer(serializers.Serializer):
    class Meta:
        model = Worker
        fields = "__all__"

        
class SaleLogSerializer(serializers.Serializer):
    class Meta:
        model = SaleLog
        fields = ["stone_type","quantity"]

class ResourceSerializer(serializers.Serializer):
    class Meta:
        model = Resource
        fields = ("resource_type" , "purchase_date", "purchase_cost", "rto_number")
    
class StoneTypeSerializer(serializers.Serializer):
    class Meta:
        model = StoneType
        fields = ("stonr_type", "price")


class DieselStockSerializer(serializers.Serializer):
    class Meta:
        model = DieselStock
        fields = "__all__"

class SaleBillSerializer(serializers.Serializer):
    class Meta:
        model = SaleBill
        fields = "__all__"