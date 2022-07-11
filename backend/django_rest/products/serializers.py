from pyexpat import model
from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'salePrice',
        ]


    def modelData(self,obj):
        print(obj.id)