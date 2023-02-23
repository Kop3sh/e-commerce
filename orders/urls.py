
from django.urls import path

from orders import views

urlpatterns = [
    path("cart/", views.cart),
    path("checkout/", views.checkout),
    path("orders/", views.OrderList.as_view()),
    path("orders/<int:pk>/", views.OrderDetail.as_view()),
]
