from django.db import models
from django.utils.translation import gettext_lazy as _


class CategoryModel(models.Model):
    name = models.CharField(max_length=54, default="", verbose_name=_(""))
    discount = models.BooleanField(default=False)
    discount_percentage = models.IntegerField(null=True, blank=True)


class BuyerModel(models.Model):
    name = models.CharField(max_length=54, default="", verbose_name=_(""))
    email = models.EmailField(max_length=54, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True


class ProductModel(models.Model):
    name = models.CharField(max_length=254, default="", verbose_name=_(""))
    description = models.TextField(
        verbose_name=_(" product description"),
    )
    price = models.IntegerField(
        null=True,
        blank=True,
    )
    discount = models.BooleanField(default=False)
    discount_percentage = models.IntegerField(null=True, blank=True)
    bought_by = models.ManyToManyField(
        BuyerModel, blank=True, related_name="buyer_products"
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        CategoryModel, on_delete=models.DO_NOTHING, related_name="products"
    )

    class Meta:
        managed = True


class SaleModel(models.Model):
    buyer = models.ForeignKey(BuyerModel, on_delete=models.CASCADE, blank=True)
    products = models.ManyToManyField(ProductModel, related_name="sales")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
