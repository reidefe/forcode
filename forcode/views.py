from typing import Dict, List, Mapping
from django.db.models import Q, Count
from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from rest_framework.decorators import action, api_view
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response

from .serializer import (
    CategorySerializer,
    ProductSerializer,
    SaleSerializer,
    BuyerSerializer,
)
from .models import SaleModel, ProductModel, CategoryModel, BuyerModel
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.views import View, APIView
from rest_framework.generics import (
    ListCreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)  # noqa
from rest_framework import serializers, status
from django.db.models import Avg, Max, query
from django.http import JsonResponse
from datetime import datetime, date

from rest_framework.generics import GenericAPIView


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.all()



class BuyerViewSet(ModelViewSet):
    serializer_class = BuyerSerializer
    queryset = BuyerModel.objects.all()


class SaleViewSet(ModelViewSet):
    serializer_class = SaleSerializer
    queryset = SaleModel.objects.all()

   

@api_view(http_method_names=['get'])
def get_purchases(request):
        purchase = SaleModel.objects.all().order_by("created").values_list()
        serializer = SaleSerializer(purchase, many=True)
        return Response({"all purchases": serializer.data})

    # return all purchases for a specific day and date in year-month-day format
@api_view(http_method_names=['get'])
def get_specific_purchase(request, date: datetime):
    if date:
        q = SaleModel.objects.filter(created=date).values_list()
        serializer = SaleSerializer(q, many=True)
        return Response({"day purchases": q})
    else:
        obj = SaleModel.objects.filter(created=datetime.date).values_list(
            "created", "products", "buyer"
        )
        serializer = SaleSerializer(obj, many=True)
        return Response(
            {
                "error message": "no purchase on specified date",
                "todays purchase": serializer.data,
            }
        )

@api_view()
def avg_category_discounted_sale( date: datetime):
    if date:
        q = (
            CategoryModel.objects.filter(created=date)
            .values_list("name", "discount", "discount_percentage", 'products', flat=True)
            .annotate(
                avg_count_discount=Count(
                    "pk", distinct=True, filter=Q(discount=False)
                )
            )
            .annotate(
                avg_count_no_discount=Count(
                    "pk", distinct=True, filter=Q(discount=True)
                )
            )
            .aggregate(Avg("avg_count_discount", "avg_count_no_discount"))
        )
        serializer = CategorySerializer(q, many=True)
        return Response({"day purchases": serializer.data})
    else:
        obj = (
            CategoryModel.objects.filter(created=datetime.now)
            .values_list("name", "discount", "discount_percentage", 'products', flat=True)
            .annotate(
                avg_count_discount=Count(
                    "products", distinct=True, filter=Q(discount=False)
                )
            )
            .annotate(
                avg_count_no_discount=Count(
                    "products", distinct=True, filter=Q(discount=True)
                )
            )
            .aggregate(Avg("avg_count_discount", "avg_count_no_discount"))
        )
        serializer = CategoryModel(obj, many=True)
        return Response(
            {
                "error message": "no purchase on specified date",
                "todays purchase": serializer.data,
            }
        )

# returns the avg amount of products sold for product discount
@api_view()
def avg_product_discounted_sale( date: datetime):
    if date:
        q = (
            ProductModel.objects.filter(created=date)
            .values_list("name", "discount", "discount_percentage")
            .annotate(
                avg_count_discount=Count(
                    "pk", distinct=True, filter=Q(discount=False)
                )
            )
            .annotate(
                avg_count_no_discount=Count(
                    "pk", distinct=True, filter=Q(discount=True)
                )
            )
            .aggregate(Avg("avg_count_discount"))
        )
        serializer = ProductModel(q, many=True)
        return Response({"day purchases": serializer.data})
    else:
        obj = (
            ProductModel.objects.filter(created=datetime.now)
            .values_list("name", "discount", "discount_percentage")
            .annotate(
                avg_count_discount=Count(
                    "pk", distinct=True, filter=Q(discount=False)
                )
            )
            .annotate(
                avg_count_no_discount=Count(
                    "pk", distinct=True, filter=Q(discount=True)
                )
            )
            .aggregate(Avg("avg_count_discount", "avg_count_no_discount"))
        )
        serializer = ProductModel(obj, many=True)
        return Response(
            {
                "error message": "no purchase on specified date",
                "todays purchase": serializer.data,
            }
        )

