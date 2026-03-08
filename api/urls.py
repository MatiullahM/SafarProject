
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register("signup", SignupViewSet, basename="signup")
router.register("dashboard", DashboardViewSet, basename="dashboard")

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path("", include(router.urls)),
]