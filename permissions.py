from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    message = 'permission id denied, you are not the owner'

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
