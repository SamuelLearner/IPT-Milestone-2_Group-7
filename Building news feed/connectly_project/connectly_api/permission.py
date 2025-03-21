from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    """Custom permission to only allow owners to edit their objects."""
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:  # Allow read-only access
            return True
        return obj.user == request.user  # Allow modifications only if the user owns the object
