from rest_framework.generics import DestroyAPIView
from products.models import Product
from rest_framework import permissions


class ProductDeleteAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user =  self.request.user

        if user.role != user.UserRole.ADMIN:
            return Product.objects.none()
        
        return Product.objects.filter(admin=user)