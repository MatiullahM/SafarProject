from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# router = DefaultRouter()
# router.register('users', UserViewSet, basename='user')


# urlpatterns = [
#     path('role-permissions/', RolePermissionsViewSet, name='role-permissions'),
#     path('roles/', RolesViewSet, name='roles'),
#     path('user-roles/', UserRolesViewSet, name='user-roles'),
#     path('permission-groups/', PermissionGroupsViewSet, name='permission-groups'),
#     path('permissions/', PermissionsViewSet, name='permissions'),
#     path('modules/', ModulesViewSet, name='modules'),
#     path('user-permissions/', UserPermissionsViewSet, name='user-permissions'),   

#     path('', include(router.urls)),

# ]


# from .views import (
#     UserViewSet,
#     ModulesViewSet,
#     PermissionGroupsViewSet,
#     PermissionsViewSet,
#     RolePermissionsViewSet,
#     RolesViewSet,
#     UserPermissionsViewSet,
#     UserRolesViewSet
# )

# router = DefaultRouter()

# router.register('users', UserViewSet, basename='user')
# router.register('modules', ModulesViewSet)
# router.register('permission-groups', PermissionGroupsViewSet)
# router.register('permissions', PermissionsViewSet)
# router.register('role-permissions', RolePermissionsViewSet)
# router.register('roles', RolesViewSet)
# router.register('user-permissions', UserPermissionsViewSet)
# router.register('user-roles', UserRolesViewSet)

# urlpatterns = router.urls

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
urlpatterns = [
    path('', include(router.urls)),
    # path('modules/', ModulesViewSet.as_view({'get': 'list', 'post': 'create'}), name='modules-list'),
    # path('modules/<int:pk>/', ModulesViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='modules-detail'),
    # path('permission-groups/', PermissionGroupsViewSet.as_view({'get': 'list', 'post': 'create'}), name='permission-groups-list'),
    # path('permission-groups/<int:pk>/', PermissionGroupsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='permission-groups-detail'),
    # path('permissions/', PermissionsViewSet.as_view({'get': 'list', 'post': 'create'}), name='permissions-list'),
    # path('permissions/<int:pk>/', PermissionsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='permissions-detail'),
    # path('role-permissions/', RolePermissionsViewSet.as_view({'get': 'list', 'post': 'create'}), name='role-permissions-list'),
    # path('role-permissions/<int:pk>/', RolePermissionsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='role-permissions-detail'),
    # path('roles/', RolesViewSet.as_view({'get': 'list', 'post': 'create'}), name='roles-list'),
    # path('roles/<int:pk>/', RolesViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='roles-detail'),
    # path('user-permissions/', UserPermissionsViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-permissions-list'),
    # path('user-permissions/<int:pk>/', UserPermissionsViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-permissions-detail'),
    # path('user-roles/', UserRolesViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-roles-list'),
    # path('user-roles/<int:pk>/', UserRolesViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-roles-detail'),
    
    

]