from rest_framework.generics import ListAPIView
from products.models import ProductOrder
from .serializers import OrderListSerializer

class OrderListAPIView(ListAPIView):
    queryset = ProductOrder.objects.all()  
    serializer_class = OrderListSerializer  