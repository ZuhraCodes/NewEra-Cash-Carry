from rest_framework import serializers
from products.models import Product

class ProductUpdateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("name", "description", "price")
