from rest_framework import serializers
from .models import ProductData  # Replace '.models' with the actual path to your 'Product' model

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductData
        fields = '__all__'
