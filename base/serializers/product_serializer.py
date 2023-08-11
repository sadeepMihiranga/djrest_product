from rest_framework import serializers

from ..models.product import Product
from .keyword_serializer import KeywordSerializer


class ProductSerializer(serializers.ModelSerializer):
    keywords = KeywordSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        # fields = ("name", "ingredients",)
        fields = '__all__'
