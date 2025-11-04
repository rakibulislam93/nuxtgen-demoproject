from django.shortcuts import render
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer,LoginSerializer,PasswordChangeSerializer,UserProfileSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from .models import Profile

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)

        return Response({
            'message':'Account create successful',
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        })


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = authenticate(email=email,password=password)
        if not user:
            return Response({'error':'Invalid credentials'},status=400)
        
        refresh = RefreshToken.for_user(user)

        return Response({
            'message':'Login successful',
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        })


# password change view 
class PasswordChangeView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PasswordChangeSerializer
    
    def post(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        old_password = serializer.validated_data['old_password']
        new_password = serializer.validated_data['new_password']
        if not user.check_password(old_password):
            return Response({'error':'Old password do not match'},status=400)
        
        user.set_password(new_password)
        user.save()
        return Response({'message':'Password change successful'},status=200)
    

# user own profile..
class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get_object(self):
        
        return Profile.objects.get(user=self.request.user)