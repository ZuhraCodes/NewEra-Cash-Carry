from rest_framework.generics import RetrieveAPIView
from products.models import ProductOrder
from .serializers import OrderDetailSerializer

class OrderDetailAPIView(RetrieveAPIView):
    queryset = ProductOrder.objects.all()  
    serializer_class = OrderDetailSerializer

    def get_queryset(self):
        return self.request.user.product_order.all()