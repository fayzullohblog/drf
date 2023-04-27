
from .models import Product
from rest_framework import serializers
from rest_framework.reverse import reverse


class ProductSerializer(serializers.ModelSerializer):
    my_discount=serializers.SerializerMethodField(read_only=True)
    url=serializers.SerializerMethodField(read_only=True)
    edit_url=serializers.HyperlinkedIdentityField(view_name='home')
    class Meta:
        model=Product
        fields=[
            'url',
            'edit_url',
            'pk',
            'title',
            'discount',
            'price',
            'my_discount',
        ]
    def get_url(self,obj):
        request=self.context.get('request')
          
        if request is None:
            return None
        return reverse('home',kwargs={'pk':obj.pk},request=request)
    def get_edit_url(self,obj):
        request=self.context.get('request')
          
        if request is None:
            return None
        return reverse('home',kwargs={'pk':obj.pk},request=request)
        

        



    def get_my_discount(self,obj):
        try:
            return obj.get_discount()
        except:
            return None
    

    

     