from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

# from ..serializers.product_serializer import ProductSerializer
# from ..models.product import Product
from ..services.product_service import get_product, get_products


# Create your views here.

@api_view(['GET'])
def get_all_view(request):
    # products = Product.objects.all()
    # serializer = ProductSerializer(products, many=True)
    return Response(get_products())


@api_view(['GET'])
def get_product_view(request, product_id):
    # product = Product.objects.get(id=product_id)
    # serializer = ProductSerializer(product, many=False)
    return Response(get_product(product_id))
