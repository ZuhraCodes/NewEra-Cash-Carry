from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cover = models.ImageField(upload_to="images/", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
    

class ProductOrder(models.Model):
    class OrderStatusChoice(models.TextChoices):
        PENDING = "pending", "Pending"
        DELIVERING = "delivering", "Delivering"
        DELIVERED = "delivered", "Delivered"
        CANCELLED = "cancelled", "Cancelled"
        FAILED = "failed", "Failed"
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_orders")
    customer = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="product_order")
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    status = models.CharField(max_length=20, choices=OrderStatusChoice.choices, default=OrderStatusChoice.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Product Order"
        verbose_name_plural = "Product Orders"

    def __str__(self):
        return f"Order {self.id} - {self.product.name} by {self.customer.username}"
    
    