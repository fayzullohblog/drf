from api.viewset import ProductGenericViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('product-router',ProductGenericViewSet,basename='product-router')
urlpatterns = router.urls
