from __future__ import unicode_literals
from .serializers import UserSerializer, CrustSerializer
from rest_framework import permissions


class delete_permissions(permissions.BasePermission):
    serializer_class = UserSerializer

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method == "DELETE":
            if request.user.is_superuser:
                return True
            else:
                return False


# class post_permissions(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         elif request.method == "POST":
#             if request.user.is_superuser:
#                 return True
#             else:
#                 return False


class post_permissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method == "POST":
            return True


class no_permissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        else:
            return False


class patch_permissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method == "PATCH":
            return True
