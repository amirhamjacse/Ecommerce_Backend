from django.urls import path
from .views import ProductListCreateAPIView, ProductDetailAPIView

urlpatterns = [
    path('', ProductListCreateAPIView.as_view()),
    path('<uuid:id>/', ProductDetailAPIView.as_view()),
]
