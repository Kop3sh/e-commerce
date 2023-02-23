
from rest_framework import serializers

from orders.models import Order, OrderItem


class OrderItemSerialzier(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        read_only_fields = (
            "id",
            "price",
            "product",
        )
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerialzier(many=True)

    class Meta:
        model = Order
        read_only_fields = (
            "id",
            # "paid_amount",
            "user",
            # "is_ordered",
            # "ordered_at",
            "created_at",
            "updated_at"
        )
        fields = "__all__"
