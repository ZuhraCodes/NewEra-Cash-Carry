from django.urls import path
from products.api_endpoints import admin, customer

urlpatterns = [
    path("admin/product/add/", admin.AddProductAPIView.as_view(), name="products-add"),
    path("admin/product/list/", admin.ProductListAPIView.as_view(), name="product-list"),
    path("admin/product/detail/<int:pk>/", admin.ProductRetrieveAPIView.as_view(), name="product-detail"),
    path("admin/product/update/<int:pk>/", admin.ProductUpdateAPIView.as_view(), name="product-update"),
    path("admin/procuct/delete/<int:pk>", admin.ProductDeleteAPIView.as_view(), name="product-delete"),

    # Customers API's
    path("customers/product/list", customer.ProductListAPIView.as_view(), name="products-list"),

]