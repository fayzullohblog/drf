from .serializer import ProductSerializer
from rest_framework import viewsets,mixins
from .models import Product

class ProductGenericViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    # lookup_field='pk'