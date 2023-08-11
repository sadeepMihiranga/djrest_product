from django.db import models
from .product import Product


class Keyword(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="keywords",)
    priority = models.BooleanField()
    status = models.CharField(max_length=20, null=False, blank=False, default='ACTIVE')

    def __str__(self):
        return self.name
