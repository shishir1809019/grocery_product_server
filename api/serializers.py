from rest_framework import serializers
from .models import ProductData

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductData
        fields = '__all__'
