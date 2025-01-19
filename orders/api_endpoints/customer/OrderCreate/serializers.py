from rest_framework import serializers
from products.models import ProductOrder
from rest_framework.exceptions import ValidationError


class OrderCreateSerializer(serializers.ModelSerializer):
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = ProductOrder
        fields = ("product", "quantity", "total_price")
    
    def validate_quantity(self, value):
        if value <= 0:
            raise ValidationError("Quantity must be at least 1")
        return value
    
    def validate(self, data):
        product = data["product"]
        quantity = data["quantity"]

        if product.stock < quantity:
            raise serializers.ValidationError({"error": "Not enough stock for this product."})

        data["total_price"] = product.price * quantity
        return data

    def create(self, validated_data):
        product = validated_data["product"]
        quantity = validated_data["quantity"]

        product.stock -= quantity
        product.save()

        customer = self.context["request"].user
        return ProductOrder.objects.create(customer=customer, **validated_data)