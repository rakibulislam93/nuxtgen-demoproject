from django.shortcuts import render
from rest_framework import generics
from . import serializers
from .models import Device
from .permissions import IsAdminOrStaff,IsAdminOrStaffOrReadOnlyOwner
from rest_framework.permissions import IsAuthenticated
# Create your views here.

# add new device..
class DeviceCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated,IsAdminOrStaff]
    serializer_class = serializers.DeviceSerializer
    

# admin / staff see all device but user only see this own device...
class DeviceListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.DeviceSerializer

    def get_queryset(self):
        user = self.request.user
        if not user.is_staff and user.user_role == 'user': # check user role
            return Device.objects.filter(user=user)
        return Device.objects.all()



class DeviceDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminOrStaffOrReadOnlyOwner]
    serializer_class = serializers.DeviceSerializer
    queryset = Device.objects.all()