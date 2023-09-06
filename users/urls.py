from django.urls import path

from users.apps import UsersConfig
from users.views import UserListAPIView, UserCreateAPIView, UserUpdateAPIView

app_name = UsersConfig.name


urlpatterns = [
    path('', UserListAPIView.as_view(), name='user_list'),
    path('create', UserCreateAPIView.as_view(), name='user_create'),
    path('update/<int:pk>', UserUpdateAPIView.as_view(), name='user_update'),
]
