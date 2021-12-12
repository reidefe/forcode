# Generated by Django 4.0 on 2021-12-10 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BuyerModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="", max_length=54, verbose_name="")),
                ("email", models.EmailField(max_length=54, unique=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
            options={
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="CategoryModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="", max_length=54, verbose_name="")),
                ("discount", models.BooleanField(default=False)),
                (
                    "discount_percentage",
                    models.IntegerField(blank=True, max_length=3, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="", max_length=254, verbose_name="")),
                ("description", models.TextField(verbose_name=" product description")),
                ("price", models.IntegerField(blank=True, max_length=10, null=True)),
                ("discount", models.BooleanField(default=False)),
                (
                    "discount_percentage",
                    models.IntegerField(blank=True, max_length=3, null=True),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "bought_by",
                    models.ManyToManyField(
                        blank=True,
                        related_name="buyer_products",
                        to="forcode.BuyerModel",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="products",
                        to="forcode.categorymodel",
                    ),
                ),
            ],
            options={
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="SaleModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "buyer",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="forcode.buyermodel",
                    ),
                ),
                (
                    "products",
                    models.ManyToManyField(
                        related_name="sales", to="forcode.ProductModel"
                    ),
                ),
            ],
            options={
                "managed": True,
            },
        ),
    ]
