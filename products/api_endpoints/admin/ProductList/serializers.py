from rest_framework import serializers
from products.models import Product

class ProductListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "description", "stock", "price")

