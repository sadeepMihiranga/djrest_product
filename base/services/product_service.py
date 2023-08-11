from ..serializers.product_serializer import ProductSerializer
from ..models.product import Product


def get_products():
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return serializer.data


def get_product(product_id):
    product = Product.objects.get(id=product_id)
    serializer = ProductSerializer(product, many=False)
    return serializer.data
