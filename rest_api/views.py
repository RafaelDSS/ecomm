from rest_framework import viewsets, mixins, generics, views, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_api.serializers import (
    CategoryModelSerializer,
    ProductModelSerializer,
    OrderModelSerializer,
)
from rest_api.api_permissions import OnlyAdminCanCreate
from products.models import Category, Order, Product


class ProductApiViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


class CategoryListOnlyAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class OrderAPIView(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, OnlyAdminCanCreate]

    def post(self, request):
        serializer = OrderModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, order_id):
        if not order_id:
            orders = Order.objects.all()
            serializer = OrderModelSerializer(orders, many=True)
        else:
            order = Order.objects.get(pk=order_id)
            serializer = OrderModelSerializer(order)

        return Response(serializer.data)
