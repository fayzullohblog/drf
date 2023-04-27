
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProductSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework import mixins,generics
from .mixin import StaffEditorPermissionMixin

# Create your views here.
@api_view(['POST','GET'])
def home(request,pk=None,*args,**kwargs):
   
    if request.method=='GET':
        if pk is not None:
            obj=get_object_or_404(Product,pk=pk)
            data=ProductSerializer(obj,many=False).data
            return Response(data)
        queryset=Product.objects.all()
        data=ProductSerializer(queryset,many=True).data
        return Response(data)
        
    if request.method=='POST': 
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title=serializer.validated_data.get('title')
            price=serializer.validated_data.get('price') or None
            print('---->',title,price) 
            if price is None:
                price='2000'
            serializer.save(price=price)
            return Response(serializer.data)
        return Response({'Invalid':'Not good data'},status=400)



class ProductRetrieveApiView(
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView):
    
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    # authentication_classes=[authentication.SessionAuthentication,
    #                         TokenAuthentication] 
    # permission_classes=[IsStaffEditorPermisson]
product_retrieve=ProductRetrieveApiView.as_view()
 

class ProductCreateApiView(
    StaffEditorPermissionMixin,
    generics.CreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    def perform_create(self, serializer):
        title=serializer.validated_data.get('title')
        price=serializer.validated_data.get('price')
        if not price:
            price='100'
        serializer.save(price=price)
        return super().perform_create(serializer)
product_create=ProductCreateApiView.as_view()

class ProductListCreateApiView(
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
product_list_create=ProductListCreateApiView.as_view()


class ProductUpdateApiView(
    StaffEditorPermissionMixin,
    generics.UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def perform_update(self,serializer):
        instance=serializer.save()
        if not instance.discount:
            instance.discount='10000000'
product_update_view=ProductUpdateApiView.as_view()

class ProductDeleteApiView(
    StaffEditorPermissionMixin,
    generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
product_delete_view=ProductDeleteApiView.as_view()

# ------------------------------------------------------------
class ProductGenericApiViewListModelMixin(generics.GenericAPIView,mixins.ListModelMixin):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
        # return super().create(request, *args, **kwargs)
product_listmixin_view=ProductGenericApiViewListModelMixin.as_view()


class ProductGenericsApiViewCreateModelMixin(generics.GenericAPIView,mixins.CreateModelMixin):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
product_createmixin_view=ProductGenericsApiViewCreateModelMixin.as_view()
    

class ProductGenericApiViewUpdateModelMixin(generics.GenericAPIView, mixins.UpdateModelMixin):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
product_updatemixin_view=ProductGenericApiViewUpdateModelMixin.as_view()