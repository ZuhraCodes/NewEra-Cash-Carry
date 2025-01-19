from django.db import models

class Order(models.Model):
    class OrderStatusChoice(models.TextChoices):
        PENDING = 'pending', 'Pending',
        DELIVERING = 'delivering', 'Delivering',
        DELIVERED = 'delivered', 'Delivered',
        FAILED = 'failed', 'Failed',
        CANCELLED = 'cancelled', 'Cancelled'

    customer = models.ForeignKey("users.User", on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=OrderStatusChoice.choices, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

class OrderDetail(models.Model):
    order = models.ForeignKey("orders.Order", related_name='order_details', on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)