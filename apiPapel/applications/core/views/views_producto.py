from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView
)
from ..models import Producto
from ..serializers import (
    ProductSerializer,
    ProductoPagination
)


# CRUD Producto

class ListProducto(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Producto.objects.all()

class PaginationListProducto(ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = ProductoPagination
    queryset = Producto.objects.all()