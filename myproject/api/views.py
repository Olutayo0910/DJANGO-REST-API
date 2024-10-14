from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework.views import APIView


# Create your views here.
class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def delete(self, request, *args, **kwargs):
        Product.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductList(APIView):
    def get(self, request, *args, **kwargs):

        name = request.query_params.get("name", "")

        if name:
            product_list = Product.objects.filter(name__icontains=name)
        else:
            product_list = Product.objects.all()

        serializer = ProductSerializer(product_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)