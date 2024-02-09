from django.urls import path
from . import views

urlpatterns = [
    path("category/", views.CategoryAPI.as_view(), name="category-list"),
    path("product/", views.ProductAPI.as_view(), name="product-list"),
    path("category/<int:pk>/", views.CategoryUpdateAPI.as_view(), name="category-update"),
    path("product/<int:pk>/", views.ProductUpdateAPI.as_view(), name="product-update"),
]
