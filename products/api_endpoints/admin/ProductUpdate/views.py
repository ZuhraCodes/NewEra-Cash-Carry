from rest_framework.generics import UpdateAPIView
from .serializers import ProductUpdateModelSerializer
from products.models import Product
from rest_framework import permissions


class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateModelSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user =  self.request.user

        if user.role != user.UserRole.ADMIN:
            return Product.objects.none()
        
        return Product.objects.filter(admin=user)