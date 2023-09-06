from django.contrib.auth.models import AbstractUser
from django.db import models

from constans import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    avatar = models.ImageField(upload_to='user/', **NULLABLE, verbose_name='avatar')
    phone = models.IntegerField(**NULLABLE, verbose_name='phone')
    city = models.CharField(**NULLABLE, max_length=100, verbose_name='city')
    is_active = models.BooleanField(default=False, verbose_name='is active')
    verification_key = models.IntegerField(**NULLABLE, verbose_name='verification')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
