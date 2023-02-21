# from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework import generics, filters, permissions
from rest_framework.response import Response

from products.serializers import ProductSerializer
from products.models import Product


# class ProductList(APIView):
#     def get(self, request, foramt=None) -> Response:
#         products = Product.objects.all()[:4]
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name"]
    ordering_fileds = ["name", "price", "created_at", "updated_at"]
    ordering = ["name"]


class ProductDetail(APIView):
    def get_object(self, pk: int) -> Product:
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk: int, format=None) -> Response:
        product = self.get_object(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


# @api_view(["POST"])
# def search(request):
#     query = request.data.get("query", "")

#     if query:
#         products = Product.objects.filter(Q(name__icontains=query))
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#     else:
#         return Response({"products": []})
