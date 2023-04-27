from api.viewset import ProductViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('product-router',ProductViewSet,basename='product-router')
urlpatterns = router.urls
