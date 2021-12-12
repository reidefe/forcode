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

# urlpatterns = [
#     path("api/genres/", GenreViews.as_view(), name="genres"),
#     # path("api/genres/<int:pk>", GenreViews().get_specific, name="genres"),
#     path("api/actors", ActorViews.as_view(), name="actors"),
#     path("api/directors/", DirectorViews.as_view(), name="directors"),
# ]
urlpatterns = router.urls
