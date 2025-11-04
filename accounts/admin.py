from django.contrib import admin
from . import models
# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'user_role', 'is_active', 'get_phone', 'get_address']

    def get_phone(self, obj):
        return obj.profile.phone if hasattr(obj, 'profile') else None
    get_phone.short_description = 'Phone'

    def get_address(self, obj):
        return obj.profile.address if hasattr(obj, 'profile') else None
    get_address.short_description = 'Address'

admin.site.register(models.CustomUser, CustomUserAdmin)
admin.site.register(models.Profile)