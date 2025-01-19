from rest_framework.generics import ListAPIView
from products.models import ProductOrder
from .serializers import OrderListSerializer

class OrderListAPIView(ListAPIView):
    queryset = ProductOrder.objects.all()  
    serializer_class = OrderListSerializer  

    def get_queryset(self):
        return self.request.user.product_order.all()