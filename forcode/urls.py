from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from .views import ProductViewSet, SaleViewSet, CategoryViewSet, BuyerViewSet, avg_category_discounted_sale, get_purchases, get_specific_purchase, avg_product_discounted_sale

router = routers.SimpleRouter()
router.register(
    r"products",
    ProductViewSet,
)
#router.register(r"sales", SaleViewSet)
router.register(
    r"category",
    CategoryViewSet,
)
router.register(
    r"buyer",
    BuyerViewSet,
)

router.register(
    r"sale",
    SaleViewSet,
)


urlpatterns = [
    re_path('sale/avg-cat-discount-sale/<date:date>', avg_category_discounted_sale),
    re_path('sale/product-avg-discount-sale/<date:date>', avg_product_discounted_sale),
    re_path('sale/get-purchases/', get_purchases),
    re_path('sale/sepcific-purchase/<date:date>', get_specific_purchase),

]
urlpatterns += router.urls
