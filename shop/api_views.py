from .models import Product
from .serializer import ProductSerializer
from rest_framework import mixins
from rest_framework import viewsets

from  rest_framework.pagination import LimitOffsetPagination

# Create your views here.


class ProductPaginationView(LimitOffsetPagination):
    default_limit=1
    max_limit=10


class ProductViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = ProductPaginationView
