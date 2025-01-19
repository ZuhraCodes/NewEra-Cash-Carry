from rest_framework.generics import RetrieveAPIView
from .serializers import ProductRetrieveModelSerializer
from products.models import Product
from rest_framework import permissions


class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductRetrieveModelSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user =  self.request.user

        if user.role != user.UserRole.ADMIN:
            return Product.objects.none()
        
        return Product.objects.filter(admin=user)