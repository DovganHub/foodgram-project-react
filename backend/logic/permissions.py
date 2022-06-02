# from rest_framework import permissions


# class AuthorOrAdminOrRead(permissions.BasePermission):

#     def has_object_permission(self, request, view, obj):
#         if (request.method in ['PUT', 'PATCH', 'DELETE'] and not
#                 request.user.is_anonymous):
#             return (
#                 request.user == obj.author
#                 or request.user.is_superuser
#             )
#         return request.method in permissions.SAFE_METHODS

#     def has_permission(self, request, view):
#         return (
#             request.method == 'POST' and
#             request.user.is_authenticated
#             or request.method in permissions.SAFE_METHODS)

from rest_framework.permissions import (BasePermission,
                                        IsAuthenticated)


class IsOwnerProfile(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_staff
        )