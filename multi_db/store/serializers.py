from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        create_category = Category.objects.using("sales").create(
            name=validated_data['name']
        )
        return create_category

    def update(self, instance, validated_data):
        instance.name = validated_data["name"]
        instance.save()
        return instance


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        create_product = Product.objects.using("sales").create(
            name=validated_data['name'],
            category=validated_data['category'],
            price=validated_data['price'],
            description=validated_data['description']
        )
        return create_product

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.category = validated_data['category']
        instance.price = validated_data['price']
        instance.description = validated_data['description']
        instance.save()
        return instance
