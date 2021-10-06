from rest_framework import viewsets


from api.products.serializers import ProductSerializer
from shop.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed.
    """

    queryset = Product.objects.all().order_by("-price")
    serializer_class = ProductSerializer
    permission_classes = []
