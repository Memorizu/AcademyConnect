import os

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user_admin = User.objects.create(
            username='boshy',
            email='kaidohmary@gmail.com',
            is_active=True,
        )

        user_admin.set_password(os.getenv('USER_PASSWORD'))
        user_admin.save()
