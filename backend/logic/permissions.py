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
from rest_framework import permissions


class AuthorOrAdminOrRead(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in ('POST', 'PATCH', 'DELETE') and
            request.user.is_authenticated
            or request.method in permissions.SAFE_METHODS)

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_superuser
            or request.user == obj.author)
