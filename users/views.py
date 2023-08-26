from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.generics import GenericAPIView, RetrieveAPIView

from django.shortcuts import render
from django.contrib.auth import login, logout, get_user_model

from . import serializers
# Create your views here.

class LoginView(views.APIView):
    permission_classes = (AllowAny, )
    serializer = serializers.LoginSerializer
    
    # what is format
    def post(self, request, format=None):
        # serializer = self.serializer(data=request.data)
        # print(self.request.data)
        # print(request.data)
        serializer = self.serializer(
            data=self.request.data, 
            context = {'reqest': self.request}
            )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        return Response(
            None, status=status.HTTP_202_ACCEPTED
        )
        

def login_view(request):
    return render(request, "login_form.html", {})


class SignUpView(GenericAPIView):
    permission_classes = (AllowAny, )
    serializer_class = serializers.SignUpSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        user_data = serializer.data
        
        return Response(user_data, status=status.HTTP_201_CREATED)

def signup_view(request):
    return render(request, "signup_form.html", {})


class LogOutView(GenericAPIView):
    
    def post(self, request):
        if not request.user.is_authenticated:
            return Response({"error": "Already Signed Out"}, status=status.HTTP_403_FORBIDDEN)
        
        logout(request)
        return Response({"done": "Signed Out Successfully"}, status=status.HTTP_200_OK)

def logout_view(request):
    return render(request, "logout_form.html", {})


class ProfileView(RetrieveAPIView):
    queryset = get_user_model()
    serializer_class = serializers.ProfileSerializer

def profile_view(request):
    return render(request, "profile_view.html", {})
