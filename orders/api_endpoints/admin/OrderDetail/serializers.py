from rest_framework import serializers
from products.models import ProductOrder

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = ['id', 'customer', 'product', 'quantity', 'total_price']
        ref_name = 'AdminOrderDetailSerializer'