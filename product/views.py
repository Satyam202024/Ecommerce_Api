from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework import viewsets

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class ProductView(APIView):
    def get(self, request):
        queryset=Product.objects.all()
        serializers=ProductSerializer(queryset,many=True)
        return Response(serializers.data)
    

class DemoView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        return Response({'success': "you are authenticated"})


class ProductByView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category__category_name']
    search_fields = ['category__pro_name']
# class ProductByView(ListAPIView):

#     queryset=Product.objects.all()
#     serializer_class=ProductSerializer
#     filterset_fields=['category_name']

        
    # def get(self, request):
    #     category = self.request.query_params.get('category')
    #     if category:    
    #         queryset = Product.objects.filter(category__category_name=category)
    #     else:
    #         queryset = Product.objects.all()
    #     serializer = ProductSerializer(queryset, many=True)
    #     return Response(serializer.data)

# class ProductByView(APIView):
#     def get(self, request):
#         category = self.request.query_params.get('category')
#         queryset = Product.objects.all()

#         if category:
#             queryset = queryset.filter(category__category_name=category)

#         serializer = ProductSerializer(queryset, many=True)
#         return Response(serializer.data)


            

