import os

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user_admin = User.objects.create(
            username='admin',
            email='admin@mail.ru',
            is_active=True,
            is_staff=True,
            is_superuser=True
        )

        user_admin.set_password(os.getenv('ADMIN_PASSWORD'))
        user_admin.save()
