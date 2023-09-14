from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

from constans import NULLABLE


class User(AbstractUser):
    username = models.CharField(max_length=150, db_index=True, **NULLABLE, verbose_name='username')
    email = models.EmailField(unique=True, verbose_name='email')
    avatar = models.ImageField(upload_to='user/', **NULLABLE, verbose_name='avatar')
    phone = models.IntegerField(**NULLABLE, verbose_name='phone')
    city = models.CharField(**NULLABLE, max_length=100, verbose_name='city')
    is_active = models.BooleanField(default=False, verbose_name='is active')
    verification_key = models.IntegerField(**NULLABLE, verbose_name='verification')
    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set_permissions')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
