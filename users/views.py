from rest_framework import generics

from academy.permissions import IsAdmin
from users.models import User
from users.permissions import UserPermission
from users.serializer import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin | UserPermission]

    # def get_serializer(self, *args, **kwargs):
    #     if self.request.user.is_staff:
    #         return AdminSerializer(*args, **kwargs)
    #     return UserSerializer(*args, **kwargs)


class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]
