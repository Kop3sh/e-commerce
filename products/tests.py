from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APIClient

from products.models import Product
from products.serializers import ProductSerializer

PRODUCTS_URL = "/api/v1/products/"


class ProductAPITest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(
            "test@bit68.com",
            "123456"
        )
        self.admin = User.objects.create_superuser(
            "admin@bit68.com",
            "123456"
        )
        self.client.force_authenticate(self.user)
        return super().setUp()

    def test_user_cannot_retrieve_products(self) -> None:
        Product.objects.create(name="tomato", price="134")
        Product.objects.create(name="potato", price="15.5")

        res = self.client.get(PRODUCTS_URL)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_only_admin_can_retrieve_products(self) -> None:
        Product.objects.create(name="tomato", price="134")
        Product.objects.create(name="potato", price="15.5")

        self.client.logout()
        self.client.force_login(self.admin)

        res = self.client.get(PRODUCTS_URL)

        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
