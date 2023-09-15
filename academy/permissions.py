from rest_framework.permissions import BasePermission

from users.models import User


class ModeratorPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name='Moderator'):
            return True
        if request.user == User.objects.filter(user=request.user):
            return True


class SuperUserPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
