from rest_framework.permissions import BasePermission


# custom permission for Admin and Staff
class IsAdminOrStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff or request.user.user_role in ['admin','staff']


# custom permission for admin, staff and device owner...
class IsAdminOrStaffOrReadOnlyOwner(BasePermission):
    """
    Admin/staff can do anything.
    Normal users can only view their own devices (read-only).
    """
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user.user_role in ['admin', 'staff']:
            return True
        
        # Normal user: only allow safe methods (GET, HEAD, OPTIONS)
        return obj.user == request.user and request.method in ['GET', 'HEAD', 'OPTIONS']