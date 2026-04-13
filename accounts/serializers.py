from rest_framework import serializers
from .models import Users
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = Users
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'password',
            'phone_number',
            'province',
            'terminal',
            'account_status',
            'last_login',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'last_login',
            'created_at',
            'updated_at',
        ]


    
        def create(self, validated_data):
            password = validated_data.pop('password')

            user = Users.objects.create(
                **validated_data,
                password=make_password(password) 
            )

            return user

# class RolePermissionsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RolePermissions
#         fields = "__all__"

# class RolesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Roles
#         fields = "__all__"  

# class UserRolesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserRoles
#         fields = "__all__"

# class PermissionGroupsSerializer(serializers.ModelSerializer): 
#     class Meta:
#         model = PermissionGroups
#         fields = "__all__"

# class PermissionsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Permissions
#         fields = "__all__"  

# class ModulesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Modules
#         fields = "__all__"


# class UserPermissionsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserPermissions
#         fields = "__all__"

