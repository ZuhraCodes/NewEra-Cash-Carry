from rest_framework import serializers
from products.models import ProductOrder

class OrderDetailSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source="product.name")
    customer = serializers.CharField(source="customer.username")

    class Meta:
        model = ProductOrder
        fields = ['id', 'customer', 'product', 'quantity', 'total_price']