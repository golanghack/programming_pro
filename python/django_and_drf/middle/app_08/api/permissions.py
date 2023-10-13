from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request: str, view: str, obj: str):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user 