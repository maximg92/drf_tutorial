from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """DRF API VIEW"""
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
    # instance = Product.objects.all().order_by("?").first()
    # data = {}
    # if instance:
    #     # data = model_to_dict(instance, fields=['id', 'title', 'price'])
    #     data = ProductSerializer(instance).data
        return Response(serializer.data)
    return Response({'invalid': 'data not good'}, status=400)


