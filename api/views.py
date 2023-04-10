
from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.forms.models import model_to_dict
from .serializer import ProductSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework import mixins
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


class ProductRetrieveApiView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
product_retrieve=ProductRetrieveApiView.as_view()
 

class ProductCreateApiView(generics.CreateAPIView):
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

class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
product_list_create=ProductListCreateApiView.as_view()


class ProductUpdateApiView(generics.UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def perform_update(self,serializer):
        instance=serializer.save()
        if not instance.discount:
            instance.discount='10000000'
product_update_view=ProductUpdateApiView.as_view()

class ProductDeleteApiView(generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
product_delete_view=ProductDeleteApiView.as_view()

# ------------------------------------------------------------
class ProductGenericApiViewMixins(generics.GenericAPIView,mixins.CreateModelMixin):
    pass