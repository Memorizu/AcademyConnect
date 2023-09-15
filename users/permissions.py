from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True

        if request.method == 'GET':
            serializer_fields = ['username', 'avatar', 'city']
            serializer = view.get_serializer(instance=obj, fields=serializer_fields)
            view.serializer_class = serializer
            return True
