from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

@api_view(["GET"])
def api_home(request,*args,**kwargs):
    instance = Product.objects.all().first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
    return Response(data)
