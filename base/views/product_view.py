from django.shortcuts import render

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

# from ..serializers.product_serializer import ProductSerializer
# from ..models.product import Product
from ..services.product_service import get_product, get_products


# Create your views here.
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])  # or can be configure as global in settings.py under REST_FRAMEWORK
def get_all_view(request):
    # products = Product.objects.all()
    # serializer = ProductSerializer(products, many=True)
    return Response(get_products())


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_product_view(request, product_id):
    # product = Product.objects.get(id=product_id)
    # serializer = ProductSerializer(product, many=False)
    return Response(get_product(product_id))
