from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.forms.models import model_to_dict
from .serializer import ProductSerializer
# Create your views here.
@api_view(['POST'])
def home(request):
    # instance=Product.objects.all().order_by('?').first()
    serializer=ProductSerializer(data=request.data)

    print('=====',serializer.is_valid())

    if serializer.is_valid():
       instance=serializer.save()
       print(instance) 
        
       return Response(serializer.data)
    
 

    