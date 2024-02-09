from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.response import Response


class CategoryAPI(generics.ListCreateAPIView):
    queryset = Category.objects.using("sales").all()
    serializer_class = CategorySerializer

    def post(self, request, *args, **kwargs):
        payload = request.data
        serializer = self.get_serializer(data=payload, context={'request': request})
        serializer.is_valid()
        serializer.save(using="sales")
        return serializer
        # return Response("category data insert success")


class CategoryUpdateAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.using("sales").all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        # import pdb
        # pdb.set_trace()
        payload = request.data
        print("category update payload:", payload)
        instance = Category.objects.using("sales").get(pk=kwargs['pk'])
        serializer = self.serializer_class(data=payload, context={'request': request})
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        category_instance = serializer.update(instance, validated_data)
        return category_instance


class ProductAPI(generics.ListCreateAPIView):
    queryset = Product.objects.using("sales").all()
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        payload = request.data
        serializer = self.get_serializer(data=payload, context={'request': request})
        serializer.save(using='sales')
        return Response("product created")


class ProductUpdateAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.using("sales").all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        payload = request.data
        instance = Product.objects.using("sales").get(pk=kwargs['pk'])
        serializer = self.serializer_class(data=payload, context={"request": request})
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        product_instance = serializer.update(instance, validated_data)
        return product_instance
