# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from products.models import Product
from products.serializers import ProductSerializer


class ProductListCreateAPIView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailAPIView(APIView):

    def get_object(self, id):
        return Product.objects.get(id=id)

    def get(self, request, id):
        product = self.get_object(id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


    def put(self, request, id):
        product = self.get_object(id)
        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        product = self.get_object(id)
        product.delete()
        return Response({"message": "Deleted successfully"})

