from django.db import models
from django.contrib.auth.models import User

from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ordered_at = models.DateField()

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.user

    @property
    def get_cart_total(self):
        order_items = self.items.all()
        return sum([item.get_total for item in order_items])

    @property
    def get_cart_items(self):
        order_items = self.items.all()
        return sum([item.quantity for item in order_items])


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.pk

    @property
    def get_total(self):
        return self.quantity * self.product.price
