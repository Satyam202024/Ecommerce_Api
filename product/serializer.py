from rest_framework import serializers
from .models import *


from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    Category = CategorySerializer()  # Nested serializer

    class Meta:
        model = Product
        exclude = []  # Exclude any fields you don't want to include


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Category
#         fields='__all__' 
 
# class ProductSerializer(serializers.ModelSerializer):
#     Category=CategorySerializer()
#     class Meta:
#         model=Product
#         fields='__all__'
