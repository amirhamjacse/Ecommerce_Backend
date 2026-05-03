from django.urls import path
from .views import (
    CartDetailAPIView,
    AddToCartAPIView,
    UpdateCartItemAPIView,
    RemoveCartItemAPIView,
    CreateOrderAPIView,
    OrderListAPIView,
    OrderDetailAPIView,
    
)

urlpatterns = [
    path('cart-detail/', CartDetailAPIView.as_view()),
    path('cart-add/', AddToCartAPIView.as_view()),
    path('cart-update/', UpdateCartItemAPIView.as_view()),
    path('cart-remove/', RemoveCartItemAPIView.as_view()),
    path('create/', CreateOrderAPIView.as_view()),
    path('list/', OrderListAPIView.as_view()),
    path('<uuid:id>/', OrderDetailAPIView.as_view()),
]