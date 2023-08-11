from django.urls import path
from .views import product_view

urlpatterns = [
    path('product/', product_view.get_all_view, name='product-list'),
    path('product/<int:product_id>/', product_view.get_product_view, name='product-detail'),
]
