from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from .views import ProductViewSet, SaleViewSet, CategoryViewSet, BuyerViewSet

router = routers.SimpleRouter()
router.register(
    r"products",
    ProductViewSet,
)
router.register(r"sales", SaleViewSet)
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
urlpatterns = router.urls
