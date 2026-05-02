from django.contrib.auth.models import Permission
from rest_framework import serializers

from .models import Role, User


class RoleSerializer(serializers.ModelSerializer):
    permissions = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Permission.objects.all(),
        required=False,
    )

    class Meta:
        model = Role
        fields = [
            "id",
            "name",
            "description",
            "permissions",
            "is_active",
            "created_at",
        ]
        read_only_fields = ["created_at"]

    def create(self, validated_data):
        permissions = validated_data.pop("permissions", [])
        role = super().create(validated_data)
        if permissions:
            role.permissions.set(permissions)
        return role

    def update(self, instance, validated_data):
        permissions = validated_data.pop("permissions", None)
        role = super().update(instance, validated_data)
        if permissions is not None:
            role.permissions.set(permissions)
        return role


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, allow_blank=False)
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["email", "username", "password", "password_confirm"]

    def validate(self, attrs):
        if attrs["password"] != attrs["password_confirm"]:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop("password_confirm")
        password = validated_data.pop("password")
        user = User.objects.create_user(password=password, **validated_data)
        return user


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, allow_blank=False)
    roles = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Role.objects.all(),
        required=False,
    )

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "password",
            "roles",
            "is_active",
            "is_staff",
            "is_superuser",
            "date_joined",
            "last_login",
        ]
        read_only_fields = ["date_joined", "last_login"]

    def create(self, validated_data):
        roles = validated_data.pop("roles", [])
        password = validated_data.pop("password", None)
        user = User.objects.create_user(password=password, **validated_data)
        if roles:
            user.roles.set(roles)
        return user

    def validate(self, attrs):
        if self.instance is None and not attrs.get("password"):
            raise serializers.ValidationError({"password": "This field is required."})
        return attrs

    def update(self, instance, validated_data):
        roles = validated_data.pop("roles", None)
        password = validated_data.pop("password", None)

        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save(update_fields=["password"])

        if roles is not None:
            user.roles.set(roles)

        return user
