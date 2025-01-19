from rest_framework import serializers
from products.models import Product
from rest_framework.exceptions import ValidationError


class AddProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "name", "description", "price")
    

    def create(self, validated_data):
        user = self.context["request"].user
        if user.role != user.UserRole.ADMIN:
            raise ValidationError({"error": "PermissionDenied", "message": "Only admin can add product"})
        validated_data["admin"] = user
        return super().create(validated_data)

