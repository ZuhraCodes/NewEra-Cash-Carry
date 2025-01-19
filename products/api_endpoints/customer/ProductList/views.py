from rest_framework.generics import ListAPIView
from products.models import Product
from .serializers import ProductListSerializer

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()  
    serializer_class = ProductListSerializer  
