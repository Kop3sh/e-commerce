from datetime import datetime
from django.http import Http404

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from orders.models import Order, OrderItem
from orders.serializers import OrderSerializer, OrderItemSerialzier

@api_view(["GET", "PUT"])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def cart(request):
    cart, items = None, None

    try:
        cart, created = Order.objects.get_or_create(is_ordered=False, user=request.user)
        items = cart.items.all()
    except OrderItem.DoesNotExist:
        items = []

    if request.method == "GET":
        serializer = OrderSerializer(cart)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = OrderSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save(is_ordered=False, user=request.uesr)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):

    cart, created = Order.objects.get_or_create(is_ordered=False, user=request.user)

    serializer = OrderSerializer(cart, data=request.data)
    if serializer.is_valid():
        paid_amount = cart.get_cart_total
        try:
            print("charge on payements API")
            serializer.save(user=request.user, paid_amount=paid_amount, is_ordered=True, ordered_at=datetime.utcnow())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            print("exception")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user, is_ordered=True)
        ser = OrderSerializer(orders, many=True)
        return Response(ser.data)


class OrderDetail(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk: int) -> Order:
        try:
            return Order.objects.filter(pk=pk, is_ordered=True)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk: int, format=None) -> Response:
        product = self.get_object(pk=pk)
        serializer = OrderSerializer(product)
        return Response(serializer.data)
