from rest_framework import serializers
from products.models import ProductOrder

class OrderListSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source="product.name")
    customer = serializers.CharField(source="customer.username")

    class Meta:
        model = ProductOrder
        fields = ['id', 'customer', 'product', 'quantity', 'total_price']
        ref_name = "AdminOrderListSerializer"