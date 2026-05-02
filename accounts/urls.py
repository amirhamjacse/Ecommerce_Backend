from django.urls import path

from .views import (
    SignUpView,
    RoleDetailAPIView,
    RoleListCreateAPIView,
    UserDetailAPIView,
    UserListCreateAPIView,
)

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("roles/", RoleListCreateAPIView.as_view(), name="role-list-create"),
    path("roles/<int:pk>/", RoleDetailAPIView.as_view(), name="role-detail"),
    path("users/", UserListCreateAPIView.as_view(), name="user-list-create"),
    path("users/<int:pk>/", UserDetailAPIView.as_view(), name="user-detail"),
]
