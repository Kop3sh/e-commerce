from django.urls import path

from products import views

urlpatterns = [
    path("products/", views.ProductListView.as_view()),
    # path("products/search", views.search),
    path("products/<int:pk>/", views.ProductDetail.as_view()),
]
