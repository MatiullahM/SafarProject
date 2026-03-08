from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status, views
from .serializers import SignupSerializer
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, login, logout,get_user_model
from django.shortcuts import redirect

class SignupViewSet(viewsets.ModelViewSet):
    # permission_classes= [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = SignupSerializer




User = get_user_model()
class LoginAPIView(APIView):
    """
    Login API using username and password only.
    Optional: Only staff/superuser can login.
    """
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            return Response(
                {"error": "Username and password are required."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Try to get user by username
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(
                {"error": "Invalid username or password"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Check password
        if not user.check_password(password):
            return Response(
                {"error": "Invalid username or password"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Optional: Only staff/superuser can login
        if not (user.is_staff or user.is_superuser):
            return Response(
                {"error": "You do not have permission to login"},
                status=status.HTTP_403_FORBIDDEN
            )
        
        # Login the user (session-based)
        login(request, user)
        return redirect(to="/api/dashboard")



class DashboardViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self, request):
        user = request.user
        return Response({
            "message": "Welcome to dashboard",
            # "email": user.email,
            # "is_staff": user.is_staff,
            # "is_superuser": user.is_superuser
        })
    
    

class LogoutAPIView(views.APIView):
  permission_classes = [IsAuthenticated]
  def get(self, request, *args, **kwargs):
    if request.user.is_authenticated:
      logout(request)
    return redirect(to="/api/login")
  