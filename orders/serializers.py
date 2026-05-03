from rest_framework import serializers
from .models import Cart, CartItem, Order, OrderItem

class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']


class OrderItemSerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = [
            'id',
            'product',
            'product_name',
            'variant',
            'price',
            'quantity'
        ]

class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'total_price',
            'status',
            'items',
            'created_at'
        ]