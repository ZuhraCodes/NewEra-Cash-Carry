from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from products.models import ProductOrder
from .serializers import OrderStatusSerializer


class OrderStatusView(RetrieveAPIView):
    queryset = ProductOrder.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = OrderStatusSerializer

    # def get_object(self):
    #     order_id = self.kwargs.get("id")
    #     try:
    #         order = ProductOrder.objects.get(id=id, customer=self.request.user)
    #     except ProductOrder.DoesNotExist:
    #         raise NotFound({"error": "Order not found or you do not have permission to view it."})
    #     return order
