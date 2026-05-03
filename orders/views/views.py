from rest_framework.views import APIView
from rest_framework.response import Response
from orders.models import Cart
from orders.serializers import CartSerializer


class CartDetailAPIView(APIView):

    def get(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)


from products.models import Product, ProductVariant
from orders.models import Cart, CartItem, Order, OrderItem


class AddToCartAPIView(APIView):

    def post(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)

        product_id = request.data.get('product_id')
        variant_id = request.data.get('variant_id')
        quantity = int(request.data.get('quantity', 1))

        product = Product.objects.get(id=product_id)
        variant = None

        if variant_id:
            variant = ProductVariant.objects.get(id=variant_id)

        item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            variant=variant,
            defaults={'quantity': quantity}
        )

        if not created:
            item.quantity += quantity
            item.save()

        return Response({"message": "Added to cart"})


class UpdateCartItemAPIView(APIView):

    def post(self, request):
        item_id = request.data.get('item_id')
        quantity = request.data.get('quantity')

        item = CartItem.objects.get(id=item_id)
        item.quantity = quantity
        item.save()

        return Response({"message": "Updated"})

class RemoveCartItemAPIView(APIView):

    def post(self, request):
        item_id = request.data.get('item_id')
        CartItem.objects.filter(id=item_id).delete()

        return Response({"message": "Removed"})

from rest_framework.views import APIView
from rest_framework.response import Response
from orders.models import Order, OrderItem, Cart
from orders.serializers import OrderSerializer, OrderItemSerializer


class CreateOrderAPIView(APIView):

    def post(self, request):

        cart = Cart.objects.get(user=request.user)
        items = cart.items.all()

        if not items:
            return Response({"error": "Cart is empty"}, status=400)

        order = Order.objects.create(
            user=request.user,
            total_price=0
        )

        total = 0

        for item in items:
            price = item.variant.price if item.variant else item.product.base_price

            OrderItem.objects.create(
                order=order,
                product=item.product,
                variant=item.variant,
                price=price,
                quantity=item.quantity
            )

            total += price * item.quantity

        order.total_price = total
        order.save()

        cart.items.all().delete()

        serializer = OrderSerializer(order)

        return Response(serializer.data)

class OrderListAPIView(APIView):

    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class OrderDetailAPIView(APIView):

    def get(self, request, id):
        order = Order.objects.get(id=id)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
