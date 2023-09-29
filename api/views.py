from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ProductData
from .serializers import ProductSerializers  # Import your ProductSerializers


class ProductList(APIView):
    """
    List all products or create a new product.
    """
    def get(self, request, format=None):
        products = ProductData.objects.all()
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
