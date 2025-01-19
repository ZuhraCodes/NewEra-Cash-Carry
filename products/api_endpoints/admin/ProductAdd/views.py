from rest_framework.generics import CreateAPIView
from rest_framework import permissions
from products.models import Product
from .serializers import AddProductSerializer

class AddProductAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = AddProductSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(customer=user)
