from rest_framework.generics import ListAPIView
from .serializers import ProductListModelSerializer
from products.models import Product
from rest_framework import permissions


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListModelSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user =  self.request.user

        if user.role != user.UserRole.ADMIN:
            return Product.objects.none()
        
        return Product.objects.filter(admin=user)