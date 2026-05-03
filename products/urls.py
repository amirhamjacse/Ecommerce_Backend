from django.urls import path
from .views import (
    ProductListCreateAPIView, ProductDetailAPIView,
    ProductListAPIView
)

urlpatterns = [
    path('', ProductListCreateAPIView.as_view()),
    path('<uuid:id>/', ProductDetailAPIView.as_view()),
    path('list/', ProductListAPIView.as_view()),
]
