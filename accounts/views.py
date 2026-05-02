from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
# from drf_yasg.utils import swagger_auto_schema
from drf_spectacular.utils import extend_schema

from .models import Role, User
from .serializers import RoleSerializer, UserSerializer, SignUpSerializer


class SignUpView(APIView):
    permission_classes = [AllowAny]

    # @swagger_auto_schema(request_body=SignUpSerializer) for other swagger library
    @extend_schema(request=SignUpSerializer)
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoleListCreateAPIView(APIView):
    def get(self, request):
        roles = Role.objects.prefetch_related("permissions").all()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoleDetailAPIView(APIView):
	def get_object(self, pk):
		return get_object_or_404(Role, pk=pk)

	def get(self, request, pk):
		role = self.get_object(pk)
		serializer = RoleSerializer(role)
		return Response(serializer.data)

	def put(self, request, pk):
		role = self.get_object(pk)
		serializer = RoleSerializer(role, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def patch(self, request, pk):
		role = self.get_object(pk)
		serializer = RoleSerializer(role, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		role = self.get_object(pk)
		role.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class UserListCreateAPIView(APIView):
    def get(self, request):
        users = User.objects.prefetch_related("roles").all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPIView(APIView):
	def get_object(self, pk):
		return get_object_or_404(User, pk=pk)

	def get(self, request, pk):
		user = self.get_object(pk)
		serializer = UserSerializer(user)
		return Response(serializer.data)

	def put(self, request, pk):
		user = self.get_object(pk)
		serializer = UserSerializer(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def patch(self, request, pk):
		user = self.get_object(pk)
		serializer = UserSerializer(user, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		user = self.get_object(pk)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
