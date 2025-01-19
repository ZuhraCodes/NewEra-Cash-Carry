from rest_framework import serializers
from products.models import ProductOrder

class OrderStatusSerializer(serializers.ModelSerializer):
    customer = serializers.CharField(source="customer.username")

    class Meta:
        model = ProductOrder
        fields = ("id", 'customer', "status", "created_at")