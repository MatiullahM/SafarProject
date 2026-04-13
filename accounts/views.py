from django.shortcuts import render
from rest_framework import viewsets
from .models import Users
from .serializers import UserSerializer
# Create your views here.



class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    

# class RolePermissionsViewSet(viewsets.ModelViewSet):
#     queryset = RolePermissions.objects.all()
#     serializer_class = RolePermissionsSerializer

# class RolesViewSet(viewsets.ModelViewSet):
#     queryset = Roles.objects.all()
#     serializer_class = RolesSerializer

# class UserRolesViewSet(viewsets.ModelViewSet):
#     queryset = UserRoles.objects.all()
#     serializer_class = UserRolesSerializer

# class PermissionGroupsViewSet(viewsets.ModelViewSet):
#     queryset = PermissionGroups.objects.all()
#     serializer_class = PermissionGroupsSerializer

# class PermissionsViewSet(viewsets.ModelViewSet):
#     queryset = Permissions.objects.all()
#     serializer_class = PermissionsSerializer

# class ModulesViewSet(viewsets.ModelViewSet):
#     queryset = Modules.objects.all()
#     serializer_class = ModulesSerializer

# class UserPermissionsViewSet(viewsets.ModelViewSet):
#     queryset = UserPermissions.objects.all()
#     serializer_class = UserPermissionsSerializer