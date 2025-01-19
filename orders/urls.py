from django.urls import path
from orders.api_endpoints import admin, customer

urlpatterns = [
    path("admin/product/orders/", admin.OrderListAPIView.as_view(), name="product-order"),
    path("admin/product/order-detail/<int:pk>/", admin.OrderDetailAPIView.as_view(), name="order-detail"),

    path("customers/order/create", customer.CustomerOrderCreateView.as_view(), name="product-order"),
    path("customers/order/list", customer.OrderListAPIView.as_view(), name="orders-list"),
    path("customer/order/detail/<int:pk>/", customer.OrderDetailAPIView.as_view(), name="order-detail"),
    path("customer/order/status/<int:pk>/", customer.OrderStatusView.as_view(), name="order-status"),
]