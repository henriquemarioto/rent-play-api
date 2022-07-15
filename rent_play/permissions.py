from rest_framework import permissions


class OwnerAndAdminPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:           
            return True

        return obj.owner == request.user or request.user.is_superuser == True

class AdminPermissions(permissions.BasePermission):
    def has_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:           
            return True

        return  request.user.is_superuser == True

class RenterAndOwnerPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:           
            return True

        return obj.renter == request.user or request.user.is_superuser == True