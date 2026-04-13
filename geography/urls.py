from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProvincesViewSet, TerminalsViewSet

router = DefaultRouter()
router.register(r'provinces', ProvincesViewSet, basename='provinces')
router.register(r'terminals', TerminalsViewSet, basename='terminals')

urlpatterns = [
    path('', include(router.urls)),
]