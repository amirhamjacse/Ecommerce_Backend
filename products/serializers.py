from rest_framework import serializers
from .models import (
    Category, ProductImage, Product,
    ProductVariant, ProductAttribute, ProductAttributeValue
)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'



class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = '__all__'


class ProductAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttribute
        fields = '__all__'


class ProductAttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeValue
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):

    variants = ProductVariantSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'category',
            'name',
            'slug',
            'base_price',
            'description',
            'is_active',
            'variants',
            'images',
        ]

    # def create(self, validated_data):
    #     variants_data = validated_data.pop('variants')
    #     images_data = validated_data.pop('images')
    #     product = Product.objects.create(**validated_data)
    #     for variant_data in variants_data:
    #         ProductVariant.objects.create(product=product, **variant_data)
    #     for image_data in images_data:
    #         ProductImage.objects.create(product=product, **image_data)
    #     return product