from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = [
            "name",
            "description",
            "price",
            "discount",
            "discount_percentage",
            "bought_by",
            "category",
        ]


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleModel
        fields = ["buyer", "products"]


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyerModel
        fields = ["name", "email"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ["name"]
