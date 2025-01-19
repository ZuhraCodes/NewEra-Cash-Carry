from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderCreateSerializer
from products.models import ProductOrder

class CustomerOrderCreateView(CreateAPIView):
    queryset = ProductOrder.objects.all()
    permission_classes = IsAuthenticated,
    serializer_class = OrderCreateSerializer

    def get_queryset(self):
        return self.request.user.product_orders.all()