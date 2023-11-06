from rest_framework import viewsets
from . import models, serializers
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer