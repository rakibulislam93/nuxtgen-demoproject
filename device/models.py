from django.db import models
from django.conf import settings

DEVICE_TYPES = (
    ('laptop','Laptop'),
    ('router','Router'),
    ('mobile','Mobile'),
    ('desktop','Desktop'),
    ('other','Other'),
)

ACTIVE_STATUS = (
    ('active','Active'),
    ('inactive','Inactive'),
    ('disconnected','Disconnected'),
)

class Device(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='devices')
    device_name = models.CharField(max_length=50)
    device_type = models.CharField(choices=DEVICE_TYPES, max_length=50) 
    mac_address = models.CharField(max_length=100, unique=True)
    ip_address = models.GenericIPAddressField()
    status = models.CharField(choices=ACTIVE_STATUS, max_length=50, default='active')
    installation_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} -- device: {self.device_name}'
